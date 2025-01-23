from .Ventana import Ventana
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import os
from datetime import datetime

class VentanaDatosProcesados(Ventana):
    def __init__(self, numero_lote, productos):
        self.numero_lote = numero_lote  # Inicializar antes de llamar a super().__init__()
        self.productos = productos  # Inicializar antes de llamar a super().__init__()
        super().__init__(title="Datos Procesados")
        self.crear_widgets()

    def crear_widgets(self):
        frame = tk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

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
        # Crear un DataFrame con los datos de los productos
        data = []
        for producto in self.productos:
            data.append([
                producto.codigo,
                producto.nombre,
                producto.codigo_barra,
                producto.tipo,
                producto.cantidad,
                producto.unidades
            ])
        
        df = pd.DataFrame(data, columns=["SKU", "Nombre", "Codigo de Barra", "Tipo", "Cantidad de paquetes", "Cantidad de unidades"])

        # Crear la carpeta en el escritorio si no existe
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        folder_path = os.path.join(desktop_path, "Recuento por lote")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Crear el archivo PDF
        pdf_path = os.path.join(folder_path, f"{self.numero_lote} - Recuento.pdf")
        doc = SimpleDocTemplate(pdf_path, pagesize=letter)
        elements = []

        # Agregar el número de lote y la fecha actual al PDF
        styles = getSampleStyleSheet()
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        elements.append(Paragraph(f"Número de Lote: {self.numero_lote}", styles['Title']))
        elements.append(Paragraph(f"Fecha de Recuento: {fecha_actual}", styles['Title']))
        elements.append(Spacer(1, 12))

        # Convertir el DataFrame a una tabla de ReportLab
        table_data = [df.columns.tolist()] + df.values.tolist()
        table = Table(table_data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(table)
        doc.build(elements)

        # Mostrar mensaje de éxito
        messagebox.showinfo("Exportación exitosa", f"PDF guardado en {pdf_path}")

        print(f"PDF guardado en {pdf_path}")