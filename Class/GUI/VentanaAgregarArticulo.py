from .Ventana import Ventana
import tkinter as tk
from tkinter import messagebox
import json

class VentanaAgregarArticulo(Ventana):
    def __init__(self):
        super().__init__(title="Agregar Artículo")

    def crear_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        label_sku = tk.Label(frame, text="SKU:", font=("Arial", 12))
        label_sku.pack(pady=5)
        vcmd_sku = (self.root.register(self.validar_sku), '%P')
        self.entry_sku = tk.Entry(frame, width=50, font=("Arial", 16), validate='key', validatecommand=vcmd_sku)
        self.entry_sku.pack(pady=5, ipady=5)

        label_nombre = tk.Label(frame, text="Nombre:", font=("Arial", 12))
        label_nombre.pack(pady=5)
        self.entry_nombre = tk.Entry(frame, width=50, font=("Arial", 16))
        self.entry_nombre.pack(pady=5, ipady=5)

        label_tipo = tk.Label(frame, text="Tipo:", font=("Arial", 12))
        label_tipo.pack(pady=5)
        vcmd_tipo = (self.root.register(self.validar_tipo), '%P')
        self.entry_tipo = tk.Entry(frame, width=50, font=("Arial", 16), validate='key', validatecommand=vcmd_tipo)
        self.entry_tipo.pack(pady=5, ipady=5)

        label_peso = tk.Label(frame, text="Peso (en gramos):", font=("Arial", 12))
        label_peso.pack(pady=5)
        vcmd_peso = (self.root.register(self.validar_peso), '%P')
        self.entry_peso = tk.Entry(frame, width=50, font=("Arial", 16), validate='key', validatecommand=vcmd_peso)
        self.entry_peso.pack(pady=5, ipady=5)

        label_cantxpaq = tk.Label(frame, text="Cantidad por paquete:", font=("Arial", 12))
        label_cantxpaq.pack(pady=5)
        vcmd_cantxpaq = (self.root.register(self.validar_cantxpaq), '%P')
        self.entry_cantxpaq = tk.Entry(frame, width=50, font=("Arial", 16), validate='key', validatecommand=vcmd_cantxpaq)
        self.entry_cantxpaq.pack(pady=5, ipady=5)

        label_codigo_barras = tk.Label(frame, text="Código de Barras (13 dígitos):", font=("Arial", 12))
        label_codigo_barras.pack(pady=5)
        vcmd_codigo_barras = (self.root.register(self.validar_codigo_barras), '%P')
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

    def validar_sku(self, texto):
        return texto.isdigit() and len(texto) <= 12 or texto == ""

    def validar_tipo(self, texto):
        return texto.isalpha() or texto == ""

    def validar_peso(self, texto):
        return texto.isdigit() or texto == ""

    def validar_cantxpaq(self, texto):
        return texto.isdigit() or texto == ""

    def validar_codigo_barras(self, texto):
        return texto.isdigit() and len(texto) <= 13 or texto == ""

    def agregar_a_nomina(self):
        sku = self.entry_sku.get()
        nombre = self.entry_nombre.get()
        tipo = self.entry_tipo.get()
        peso = self.entry_peso.get()
        cantxpaq = self.entry_cantxpaq.get()
        codigo_barras = self.entry_codigo_barras.get()

        if not sku or not nombre or not tipo or not peso or not cantxpaq or not codigo_barras:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        with open('nomina.json', 'r') as file:
            nomina = json.load(file)
        
        # Verificar si el producto ya está en la nómina
        for articulo in nomina:
            if articulo['codigo_barra'] == codigo_barras:
                messagebox.showerror("Error", "El producto con este código de barras ya está en la nómina.")
                return

        nuevo_articulo = {
            "codigo": sku,
            "nombre": nombre,
            "tipo": tipo,
            "peso": peso,
            "cantidadxPaq": cantxpaq,
            "codigo_barra": codigo_barras
        }

        nomina.append(nuevo_articulo)

        with open('nomina.json', 'w') as file:
            json.dump(nomina, file, indent=4)

        messagebox.showinfo("Éxito", "Artículo agregado a la nómina.")
        self.limpiar_campos()

    def limpiar_campos(self):
        self.entry_sku.config(validate='none')
        self.entry_peso.config(validate='none')
        self.entry_codigo_barras.config(validate='none')
        self.entry_cantxpaq.config(validate='none')
        self.entry_tipo.config(validate='none')

        self.entry_sku.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_tipo.delete(0, tk.END)
        self.entry_peso.delete(0, tk.END)
        self.entry_cantxpaq.delete(0, tk.END)
        self.entry_codigo_barras.delete(0, tk.END)

        self.entry_sku.config(validate='key', validatecommand=(self.root.register(self.validar_sku), '%P'))
        self.entry_peso.config(validate='key', validatecommand=(self.root.register(self.validar_peso), '%P'))
        self.entry_codigo_barras.config(validate='key', validatecommand=(self.root.register(self.validar_codigo_barras), '%P'))
        self.entry_cantxpaq.config(validate='key', validatecommand=(self.root.register(self.validar_cantxpaq), '%P'))
        self.entry_tipo.config(validate='key', validatecommand=(self.root.register(self.validar_tipo), '%P'))

    def volver_atras(self):
        from .VentanaVerificarCBarras import VentanaVerificarCBarras
        self.root.destroy()
        ventana_verificar_cbarras = VentanaVerificarCBarras()
        ventana_verificar_cbarras.mostrar()

    def volver_menu(self):
        from .VentanaMenuPrincipal import VentanaMenuPrincipal
        self.root.destroy()
        ventana_menu_principal = VentanaMenuPrincipal()
        ventana_menu_principal.mostrar()