from .Ventana import Ventana
from ..Producto import Producto
import tkinter as tk
from tkinter import messagebox
import json

class VentanaVerificarCBarras(Ventana):
    def __init__(self, root, window_manager):
        super().__init__(root, window_manager,title="Verificar Código de Barras")
        self.crear_widgets()

    def crear_widgets(self):
        frame = tk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        nomina = Producto.cargar_datos_nomina()
        
        
        
        

        label = tk.Label(frame, text="Ingrese el código de barras:", font=("Arial", 12))
        label.pack(pady=10)
        vcm_codigo_barras = (self.root.register(lambda texto: self.valida_numero(texto, longitud=13)), '%P')
        self.entry_codigo_barras = tk.Entry(frame, width=50, font=("Arial", 16), validate="key", validatecommand=vcm_codigo_barras)
        self.entry_codigo_barras.pack(pady=10, ipady=10)




        btn_verificar = tk.Button(frame, text="Verificar", command=self.verificar_codigo_barras, width=20, height=3, font=("Arial", 16))
        btn_verificar.pack(pady=10)

        # Crear un Frame para el Text y la Scrollbar
        text_frame = tk.Frame(frame)
        text_frame.pack(pady=10)

        self.text_articulos = tk.Text(text_frame, width=80, height=20, font=("Arial", 10), wrap=tk.WORD)
        self.text_articulos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_frame, command=self.text_articulos.yview, width=30)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_articulos.config(yscrollcommand=scrollbar.set)
        self.text_articulos.config(state=tk.DISABLED)  # Configurar como solo lectura

        # Crear un Frame para los botones
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=10)

        btn_volver_menu = tk.Button(btn_frame, text="Volver al Menú", command=self.volver_menu, width=20, height=3, font=("Arial", 16))
        btn_volver_menu.pack(side=tk.LEFT, padx=5)

        btn_agregar_articulo = tk.Button(btn_frame, text="Agregar Artículo", command=self.agregar_articulo, width=20, height=3, font=("Arial", 16))
        btn_agregar_articulo.pack(side=tk.LEFT, padx=5)
        
        self.text_articulos.config(state=tk.NORMAL)  # Habilitar edición temporalmente
        self.text_articulos.delete(1.0, tk.END)
        for idx, articulo in enumerate(nomina, start=1):
            self.text_articulos.insert(tk.END, f"Ítem {idx}:\n")
            self.text_articulos.insert(tk.END, f"SKU: {articulo.get('sku', 'N/A')}\n")
            self.text_articulos.insert(tk.END, f"Nombre: {articulo.get('nombre', 'N/A')}\n")
            self.text_articulos.insert(tk.END, f"Tipo: {articulo.get('tipo', 'N/A')}\n")
            self.text_articulos.insert(tk.END, f"Peso: {articulo.get('peso', 'N/A')}\n")
            self.text_articulos.insert(tk.END, f"Código de Barras: {articulo.get('codigo_barra', 'N/A')}\n")
            self.text_articulos.insert(tk.END, "-"*40 + "\n")
        self.text_articulos.config(state=tk.DISABLED)  # Volver a solo lectura
        
        
        
        
        

    def verificar_codigo_barras(self):
        codigo_barras = self.entry_codigo_barras.get().strip()
        Producto.verificar_codigo_barras(codigo_barras)
        
    def volver_menu(self):
        self.window_manager.show_menu_principal()

    def agregar_articulo(self):
        self.window_manager.show_agregar_articulo()