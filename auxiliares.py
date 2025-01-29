import pandas as pd
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog


# Funcion para obtener la resolucion de la pantalla
def obtener_res(root):

    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()

    return f"{w}x{h}"


# Funcion para exportar el PDF
def exportar_a_pdf(numero_lote, productos, apellido):
    # Crear un DataFrame con los datos de los productos
    data = []
    for producto in productos:
        data.append([
            producto.sku,
            producto.nombre,
            producto.codigo_barra,
            producto.tipo,
            producto.cantidad,
            producto.cantidadxPaq,
            producto.unidadesTotales
        ])
    
    df = pd.DataFrame(data, columns=["SKU", "Nombre", "Codigo de Barra", "Tipo", "Cantidad de paquetes", "Cantidad de por Paquete", "Unidades Totales"])

    # Crear la carpeta en el escritorio si no existe
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    folder_path = os.path.join(desktop_path, "Recuento por lote")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Crear el archivo PDF
    pdf_path = os.path.join(folder_path, f"{numero_lote} - Recuento.pdf")
    
    
    
    # Verificar si el archivo ya existe
    if os.path.exists(pdf_path):
        respuesta = messagebox.askyesno("Archivo existente", f"El archivo {pdf_path} ya existe. ¿Desea sobrescribirlo?")
        if not respuesta:
            nuevo_nombre = simpledialog.askstring("Guardar como", "Ingrese el nuevo nombre para el archivo:")
            if nuevo_nombre:
                pdf_path = os.path.join(folder_path, f"{nuevo_nombre}.pdf")
            else:
                messagebox.showinfo("Cancelado", "La exportación ha sido cancelada.")
                return
    
    
    doc = SimpleDocTemplate(pdf_path, pagesize=landscape(letter))
    elements = []

    # Agregar el número de lote y la fecha actual al PDF
    styles = getSampleStyleSheet()
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    elements.append(Paragraph(f"Apellido del usuario: {apellido}", styles['Title']))
    elements.append(Paragraph(f"Número de Lote: {numero_lote}", styles['Title']))
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


