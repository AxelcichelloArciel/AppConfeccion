from .Ventana import Ventana
import tkinter as tk
from tkinter import messagebox
import json

class VentanaAgregarArticulo(Ventana):
    def __init__(self):
        super().__init__(title="Agregar Artículo")
        self.crear_widgets()

    def crear_widgets(self):
        frame = tk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label_sku = tk.Label(frame, text="SKU (12 dígitos):", font=("Arial", 12))
        label_sku.pack(pady=5)
        vcmd_sku = (self.root.register(self.validar_sku), '%P')
        self.entry_sku = tk.Entry(frame, width=50, font=("Arial", 16), validate='key', validatecommand=vcmd_sku)
        self.entry_sku.pack(pady=5, ipady=5)

        label_nombre = tk.Label(frame, text="Nombre:", font=("Arial", 12))
        label_nombre.pack(pady=5)
        self.entry_nombre = tk.Entry(frame, width=50, font=("Arial", 16))
        self.entry_nombre.pack(pady=5, ipady=5)

        label_peso = tk.Label(frame, text="Peso (en gramos):", font=("Arial", 12))
        label_peso.pack(pady=5)
        vcmd_peso = (self.root.register(self.validar_peso), '%P')
        self.entry_peso = tk.Entry(frame, width=50, font=("Arial", 16), validate='key', validatecommand=vcmd_peso)
        self.entry_peso.pack(pady=5, ipady=5)

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

    def validar_sku(self, entrada):
        return entrada.isdigit() and len(entrada) <= 12

    def validar_peso(self, entrada):
        return entrada.isdigit()

    def validar_codigo_barras(self, entrada):
        return entrada.isdigit() and len(entrada) <= 13

    def agregar_a_nomina(self):
        sku = self.entry_sku.get().strip()
        nombre = self.entry_nombre.get().strip()
        peso = self.entry_peso.get().strip()
        codigo_barras = self.entry_codigo_barras.get().strip()

        if not sku or not nombre or not peso or not codigo_barras:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if len(sku) != 12:
            messagebox.showerror("Error", "El SKU debe tener 12 dígitos.")
            return

        if len(codigo_barras) != 13:
            messagebox.showerror("Error", "El código de barras debe tener 13 dígitos.")
            return

        nuevo_articulo = {
            "sku": sku,
            "nombre": nombre,
            "peso": f"{peso} gr.",
            "codigo_barra": codigo_barras
        }

        try:
            with open('nomina.json', 'r') as file:
                nomina = json.load(file)
        except FileNotFoundError:
            nomina = []

        # Validar que no se repita ni el SKU ni el código de barras
        for item in nomina:
            if 'sku' in item and item['sku'] == sku:
                messagebox.showerror("Error", f"El SKU {sku} ya existe en la nómina.")
                return
            if 'codigo_barra' in item and item['codigo_barra'] == codigo_barras:
                messagebox.showerror("Error", f"El código de barras {codigo_barras} ya existe en la nómina.")
                return

        nomina.append(nuevo_articulo)

        with open('nomina.json', 'w') as file:
            json.dump(nomina, file, indent=4)

        messagebox.showinfo("Éxito", "Artículo agregado a la nómina.")
        self.limpiar_campos()

    def limpiar_campos(self):
        self.entry_sku.config(validate='none')
        self.entry_peso.config(validate='none')
        self.entry_codigo_barras.config(validate='none')

        self.entry_sku.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_peso.delete(0, tk.END)
        self.entry_codigo_barras.delete(0, tk.END)

        self.entry_sku.config(validate='key', validatecommand=(self.root.register(self.validar_sku), '%P'))
        self.entry_peso.config(validate='key', validatecommand=(self.root.register(self.validar_peso), '%P'))
        self.entry_codigo_barras.config(validate='key', validatecommand=(self.root.register(self.validar_codigo_barras), '%P'))

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