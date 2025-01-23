from .Ventana import Ventana
import tkinter as tk
from tkinter import messagebox
import json

class VentanaVerificarCBarras(Ventana):
    def __init__(self):
        super().__init__(title="Verificar Código de Barras")
        self.crear_widgets()

    def crear_widgets(self):
        frame = tk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label = tk.Label(frame, text="Ingrese el código de barras:", font=("Arial", 12))
        label.pack(pady=10)

        self.entry_codigo_barras = tk.Entry(frame, width=50, font=("Arial", 16))
        self.entry_codigo_barras.pack(pady=10, ipady=10)
        self.entry_codigo_barras.bind("<KeyRelease>", self.validar_entrada)

        btn_verificar = tk.Button(frame, text="Verificar", command=self.verificar_codigo_barras, width=20, height=3, font=("Arial", 16))
        btn_verificar.pack(pady=10)

        self.text_articulos = tk.Text(frame, width=80, height=20, font=("Arial", 10), wrap=tk.WORD)
        self.text_articulos.pack(pady=10)

        # Crear un Frame para los botones
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=10)

        btn_volver_menu = tk.Button(btn_frame, text="Volver al Menú", command=self.volver_menu, width=20, height=3, font=("Arial", 16))
        btn_volver_menu.pack(side=tk.LEFT, padx=5)

        btn_agregar_articulo = tk.Button(btn_frame, text="Agregar Artículo", command=self.agregar_articulo, width=20, height=3, font=("Arial", 16))
        btn_agregar_articulo.pack(side=tk.LEFT, padx=5)

        self.cargar_articulos()

    def validar_entrada(self, event):
        entrada = self.entry_codigo_barras.get()
        if not entrada.isdigit():
            self.entry_codigo_barras.delete(0, tk.END)
            self.entry_codigo_barras.insert(0, ''.join(filter(str.isdigit, entrada)))
        if len(entrada) > 13:
            self.entry_codigo_barras.delete(13, tk.END)

    def cargar_articulos(self):
        # Cargar los artículos desde el archivo nomina.json
        with open('nomina.json', 'r') as file:
            nomina = json.load(file)

        # Listar todos los artículos con su identificador de ítem
        for idx, item in enumerate(nomina):
            self.text_articulos.insert(tk.END, f"Item {idx + 1}: {item['nombre']} (Código de Barras: {item['codigo_barra']})\n")

        self.text_articulos.config(state=tk.DISABLED)  # Hacer el widget Text de solo lectura

    def verificar_codigo_barras(self):
        codigo_barras = self.entry_codigo_barras.get().strip()
        if not codigo_barras:
            messagebox.showerror("Error", "El campo de código de barras no puede estar vacío.")
            return

        # Cargar los artículos desde el archivo nomina.json
        with open('nomina.json', 'r') as file:
            nomina = json.load(file)

        # Verificar si el código de barras está cargado
        for idx, item in enumerate(nomina):
            if item['codigo_barra'] == codigo_barras:
                messagebox.showinfo("Resultado", f"El código de barras {codigo_barras} está cargado en el ítem {idx + 1}: {item['nombre']}")
                return

        messagebox.showinfo("Resultado", f"El código de barras {codigo_barras} no está cargado en la nómina.")

    def volver_menu(self):
        from .VentanaMenuPrincipal import VentanaMenuPrincipal
        ventana_menu_principal = VentanaMenuPrincipal()
        self.root.destroy()
        ventana_menu_principal.mostrar()

    def agregar_articulo(self):
        from .VentanaAgregarArticulo import VentanaAgregarArticulo
        ventana_agregar_articulo = VentanaAgregarArticulo()
        self.root.destroy()
        ventana_agregar_articulo.mostrar()