from .Ventana import Ventana
import tkinter as tk
from tkinter import messagebox
from auxiliares import exportar_a_pdf
import sys
import os

# Agregar la ruta del directorio principal al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


class VentanaDatosProcesados(Ventana):
    def __init__(self, numero_lote, productos, apellido):
        self.numero_lote = numero_lote  # Inicializar antes de llamar a super().__init__()
        self.productos = productos  # Inicializar antes de llamar a super().__init__()
        self.apellido = apellido  # Inicializar antes de llamar a super().__init__()
        super().__init__(title="Datos Procesados")
        self.crear_widgets()

    def crear_widgets(self):
        frame = tk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label_lote = tk.Label(frame, text=f"Apellido: {self.apellido}", font=("Arial", 12))
        label_lote.pack(pady=10)

        label_lote = tk.Label(frame, text=f"Número de Lote: {self.numero_lote}", font=("Arial", 12))
        label_lote.pack(pady=10)

        # Crear un widget Text para mostrar los productos
        self.text_productos = tk.Text(frame, width=80, height=20, font=("Arial", 10), wrap=tk.WORD)
        self.text_productos.pack(pady=10)

        # Formatear y agregar los productos al widget Text
        for producto in self.productos:
            self.text_productos.insert(tk.END, f"SKU: {producto.codigo}\n")
            self.text_productos.insert(tk.END, f"Nombre: {producto.nombre}\n")
            self.text_productos.insert(tk.END, f"Codigo de Barra: {producto.codigo_barra}\n")
            self.text_productos.insert(tk.END, f"Tipo: {producto.tipo}\n")
            self.text_productos.insert(tk.END, f"Cantidad de paquetes: {producto.cantidad}\n")
            self.text_productos.insert(tk.END, f"Cantidad de unidades: {producto.unidades}\n")
            self.text_productos.insert(tk.END, "-"*40 + "\n")

        self.text_productos.config(state=tk.DISABLED)  # Hacer el widget Text de solo lectura

        btn_cerrar = tk.Button(frame, text="Menu Principal", command=self.cerrar_ventana, width=20, height=3, font=("Arial", 16))
        btn_cerrar.pack(pady=10)

        btn_imprimir = tk.Button(frame, text="Exportar a PDF", command=self.imprimir, width=20, height=3, font=("Arial", 16))
        btn_imprimir.pack(pady=10)

    def cerrar_ventana(self):
        from .VentanaMenuPrincipal import VentanaMenuPrincipal
        self.root.destroy()  # Destruir la ventana
        ventana_menu_principal = VentanaMenuPrincipal()
        ventana_menu_principal.mostrar()

    def imprimir(self):
        # Exportar a PDF usando la función auxiliar
        pdf_path = exportar_a_pdf(self.numero_lote, self.productos, self.apellido)

        # Mostrar mensaje de éxito
        messagebox.showinfo("Exportación exitosa", f"PDF guardado en {pdf_path}")

        print(f"PDF guardado en {pdf_path}")