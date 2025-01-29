from .Ventana import Ventana
import tkinter as tk
from ..Producto import Producto
from tkinter import messagebox
import json

class VentanaAgregarArticulo(Ventana):
    def __init__(self, root, window_manager):
        super().__init__(root, window_manager, title="Agregar Artículo")

    def crear_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Agrega el SKU
        label_sku = tk.Label(frame, text="SKU:", font=("Arial", 12))
        label_sku.pack(pady=5)
        vcmd_sku = (self.root.register(lambda texto: self.valida_numero(texto, longitud=12)), '%P')
        self.entry_sku = tk.Entry(frame, width=50, font=("Arial", 16), validate='key', validatecommand=vcmd_sku)
        self.entry_sku.pack(pady=5, ipady=5)

        label_nombre = tk.Label(frame, text="Nombre:", font=("Arial", 12))
        label_nombre.pack(pady=5)
        self.entry_nombre = tk.Entry(frame, width=50, font=("Arial", 16))
        self.entry_nombre.pack(pady=5, ipady=5)

        label_tipo = tk.Label(frame, text="Tipo:", font=("Arial", 12))
        label_tipo.pack(pady=5)
        vcmd_tipo = (self.root.register(self.valida_texto), '%P')
        self.entry_tipo = tk.Entry(frame, width=50, font=("Arial", 16), validate='key', validatecommand=vcmd_tipo)
        self.entry_tipo.pack(pady=5, ipady=5)

        label_peso = tk.Label(frame, text="Peso (en gramos):", font=("Arial", 12))
        label_peso.pack(pady=5)
        vcmd_peso = (self.root.register(lambda texto: self.valida_numero(texto, longitud=7)), '%P')
        self.entry_peso = tk.Entry(frame, width=50, font=("Arial", 16), validate='key', validatecommand=vcmd_peso)
        self.entry_peso.pack(pady=5, ipady=5)

        label_cantxpaq = tk.Label(frame, text="Cantidad por paquete:", font=("Arial", 12))
        label_cantxpaq.pack(pady=5)
        vcmd_cantxpaq = (self.root.register(lambda texto: self.valida_numero(texto, longitud=3)), '%P')
        self.entry_cantxpaq = tk.Entry(frame, width=50, font=("Arial", 16), validate='key', validatecommand=vcmd_cantxpaq)
        self.entry_cantxpaq.pack(pady=5, ipady=5)

        label_codigo_barras = tk.Label(frame, text="Código de Barras (13 dígitos):", font=("Arial", 12))
        label_codigo_barras.pack(pady=5)
        vcmd_codigo_barras = (self.root.register(lambda texto: self.valida_numero(texto, longitud=13)), '%P')
        self.entry_codigo_barras = tk.Entry(frame, width=50, font=("Arial", 16), validate='key', validatecommand=vcmd_codigo_barras)
        self.entry_codigo_barras.pack(pady=5, ipady=5)

        btn_agregar = tk.Button(frame, text="Agregar a la Nómina", command=self.agregar_a_nomina, width=20, height=3, font=("Arial", 16))
        btn_agregar.pack(pady=10)

        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=10)

        btn_volver_atras = tk.Button(btn_frame, text="Volver Atrás", command=self.volver_atras, width=20, height=3, font=("Arial", 16))
        btn_volver_atras.pack(side=tk.LEFT, padx=5)

        btn_volver_menu = tk.Button(btn_frame, text="Volver al Menú", command=self.volver_menu, width=20, height=3, font=("Arial", 16))
        btn_volver_menu.pack(side=tk.LEFT, padx=5)
        
        
    def agregar_a_nomina(self):
        sku = self.entry_sku.get()
        nombre = self.entry_nombre.get()
        tipo = self.entry_tipo.get()
        peso = self.entry_peso.get()
        cantxpaq = self.entry_cantxpaq.get()
        codigo_barras = self.entry_codigo_barras.get()
        
        producto = Producto(sku, nombre, codigo_barras, cantxpaq, tipo, peso)
        resultado = producto.agregar_a_nomina()
        
        if resultado is True: 
            self.limpiar_campos()
            

    def volver_atras(self):
        self.window_manager.show_verificar_cbarras()

    def volver_menu(self):
        self.window_manager.show_menu_principal()