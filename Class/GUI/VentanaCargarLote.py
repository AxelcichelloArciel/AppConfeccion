from .Ventana import Ventana
from ..Producto import Producto
from .VentanaDatosProcesados import VentanaDatosProcesados
import tkinter as tk
from tkinter import messagebox
from collections import Counter
import json

class VentanaCargarLote(Ventana):
    def __init__(self):
        super().__init__(title="Cargar Lote")
        self.crear_widgets()
        self.cargar_datos_nomina()

    def crear_widgets(self):
        frame = tk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label_apellido = tk.Label(frame, text="Ingrese su apellido:", font=("Arial", 12))
        label_apellido.pack(pady=10)

        self.entry_apellido = tk.Entry(frame, width=50, font=("Arial", 16))
        self.entry_apellido.pack(pady=10, ipady=10)
        self.entry_apellido.bind("<KeyRelease>", self.validar_entrada_apellido)

        label_lote = tk.Label(frame, text="Ingrese el número de lote:", font=("Arial", 12))
        label_lote.pack(pady=10)

        self.entry_lote = tk.Entry(frame, width=50, font=("Arial", 16))
        self.entry_lote.pack(pady=10, ipady=10)
        self.entry_lote.bind("<KeyRelease>", self.validar_entrada_lote)

        label = tk.Label(frame, text="Ingrese los números de SKU (cadena continua de 13 dígitos cada uno):", font=("Arial", 12))
        label.pack(pady=10)

        # Crear un Frame para el Text y la Scrollbar
        text_frame = tk.Frame(frame)
        text_frame.pack(pady=10)

        self.text = tk.Text(text_frame, width=50, height=15, font=("Arial", 16), wrap=tk.WORD)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar_y = tk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.text.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.config(yscrollcommand=scrollbar_y.set)

        # Crear un Frame para los botones
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=10)

        btn_procesar = tk.Button(btn_frame, text="Procesar lote", command=self.procesar_datos, width=20, height=3, font=("Arial", 16))
        btn_procesar.pack(side=tk.LEFT, padx=5)

        btn_volver = tk.Button(btn_frame, text="Volver", command=self.volver_atras, width=20, height=3, font=("Arial", 16))
        btn_volver.pack(side=tk.LEFT, padx=5)

        self.text.bind("<KeyRelease>", self.formatear_y_validar_texto)

    def cargar_datos_nomina(self):
        with open('nomina.json', 'r') as file:
            self.datos_nomina = json.load(file)

    def validar_entrada_apellido(self, event):
        contenido = self.entry_apellido.get()
        if not contenido.isalpha():
            self.entry_apellido.delete(0, tk.END)
            self.entry_apellido.insert(0, ''.join(filter(str.isalpha, contenido)))
    
    def validar_entrada_lote(self, event):
        contenido = self.entry_lote.get()
        if not contenido.isdigit():
            self.entry_lote.delete(0, tk.END)
            self.entry_lote.insert(0, ''.join(filter(str.isdigit, contenido)))

    def formatear_y_validar_texto(self, event):
        contenido = self.text.get("1.0", tk.END).replace('\n', '').replace('\r', '').replace(' ', '')
        contenido = ''.join(filter(str.isdigit, contenido))
        formateado = ''
        for i in range(0, len(contenido), 13):
            formateado += contenido[i:i+13] + '\n'
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", formateado.strip())

    def validar_codigos_sku(self):
        skus = self.text.get("1.0", tk.END).strip().split()
        codigos_nomina = {producto['codigo_barra'] for producto in self.datos_nomina}
        for sku in skus:
            if sku not in codigos_nomina:
                return False, sku
        return True, None

    def procesar_datos(self):
        # Validar que el campo de SKU no esté vacío
        if not self.text.get("1.0", tk.END).strip():
            messagebox.showerror("Error", "Debe ingresar al menos un codigo de barras.")
            return

        valido, sku_invalido = self.validar_codigos_sku()
        if not valido:
            messagebox.showerror("Error", f"El código SKU {sku_invalido} no es válido.")
            return

        apellido = self.entry_apellido.get().strip()
        if not apellido:
            messagebox.showerror("Error", "El apellido no puede estar vacío.")
            return

        numero_lote = self.entry_lote.get().strip()
        if not numero_lote:
            messagebox.showerror("Error", "El número de lote no puede estar vacío.")
            return

        entrada = self.text.get("1.0", tk.END).strip().replace('\n', '').replace('\r', '').replace(' ', '')
        if len(entrada) % 13 != 0:
            messagebox.showerror("Error", "La cadena no es múltiplo de 13.")
            return
        
        numeros = [entrada[i:i+13] for i in range(0, len(entrada), 13)]
        conteo = Counter(numeros)

        with open('nomina.json', 'r') as file:
            nomina = json.load(file)

        nomina_dict = {item['codigo_barra']: item for item in nomina}

        productos = []

        for numero, cantidad in conteo.items():
            if numero in nomina_dict:
                sku = nomina_dict[numero]['codigo']
                nombre = nomina_dict[numero]['nombre']
                producto = Producto(codigo=sku, nombre=nombre, codigo_barra=numero, cantidad=cantidad)
                productos.append(producto)
            else:
                print(f"Código de barras: {numero} no se encontró en la nómina")

        ventana_datos_procesados = VentanaDatosProcesados(numero_lote, productos, apellido)
        self.root.destroy()
        ventana_datos_procesados.mostrar()
        self.root.quit()

    def volver_atras(self):
        from .VentanaMenuPrincipal import VentanaMenuPrincipal

        ventana_menu_principal = VentanaMenuPrincipal()
        self.root.destroy()  # Cierra la ventana actual
        ventana_menu_principal.mostrar()
        self.root.quit()

