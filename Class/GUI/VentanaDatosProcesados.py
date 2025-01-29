from .Ventana import Ventana
import tkinter as tk
from tkinter import messagebox
import auxiliares as aux
import sys
import os

# Agregar la ruta del directorio principal al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


class VentanaDatosProcesados(Ventana):
    def __init__(self, root, window_manager, numero_lote, productos, apellido):
        self.numero_lote = numero_lote  # Inicializar antes de llamar a super().__init__()
        self.productos = productos  # Inicializar antes de llamar a super().__init__()
        self.apellido = apellido  # Inicializar antes de llamar a super().__init__()
        super().__init__(root, window_manager, title="Datos Procesados")

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
            self.text_productos.insert(tk.END, f"SKU: {producto.sku}\n")
            self.text_productos.insert(tk.END, f"Nombre: {producto.nombre}\n")
            self.text_productos.insert(tk.END, f"Codigo de barra: {producto.codigo_barra}\n")
            self.text_productos.insert(tk.END, f"Tipo: {producto.tipo}\n")
            self.text_productos.insert(tk.END, f"Cantidad de paquetes contados: {producto.cantidad}\n")
            self.text_productos.insert(tk.END, f"Unidades por paquete: {producto.cantidadxPaq}\n")
            self.text_productos.insert(tk.END, f"Unidades totales: {producto.unidadesTotales}\n")
            self.text_productos.insert(tk.END, "-"*40 + "\n")

        self.text_productos.config(state=tk.DISABLED)  # Hacer el widget Text de solo lectura

        btn_cerrar = tk.Button(frame, text="Menu Principal", command=self.cerrar_ventana, width=20, height=3, font=("Arial", 16))
        btn_cerrar.pack(pady=10)

        btn_imprimir = tk.Button(frame, text="Exportar a PDF", command=lambda: aux.exportar_a_pdf(self.numero_lote, self.productos, self.apellido), width=20, height=3, font=("Arial", 16))
        btn_imprimir.pack(pady=10)

    def cerrar_ventana(self):
        self.window_manager.show_menu_principal()

    
        