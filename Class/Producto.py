import json
from tkinter import messagebox
from .GUI.Ventana import Ventana
from tkinter import messagebox, simpledialog

class Producto:
    def __init__(self, sku, nombre, codigo_barra, cantidadxPaq, tipo, peso, cantidad = 0, unidadesTotales = 0):
        self.sku = sku
        self.nombre = nombre
        self.codigo_barra = codigo_barra
        self.cantidadxPaq = int(cantidadxPaq) # Convertir a entero, por que en la nomina es un string
        self.tipo = tipo
        self.peso = peso
        self.cantidad = int(cantidad)
        self.unidadesTotales = int(unidadesTotales)

    def __repr__(self):
        return f"Producto(sku={self.sku}, nombre={self.nombre}, codigo_barra={self.codigo_barra}, cantidadxPaq={self.cantidadxPaq}, tipo={self.tipo}, peso={self.peso}, cantidad={self.cantidad}, unidadesTotales={self.unidadesTotales})"
    
    @staticmethod
    def cargar_datos_nomina():
        with open('nomina.json', 'r') as file:
            datos_nomina = json.load(file)
            return datos_nomina
    
    # Metodo que agrega un articulo a la nomina
    def agregar_a_nomina(self):
        
        sku = self.sku
        nombre = self.nombre
        codigo_barra = self.codigo_barra
        cantxpaq = self.cantidadxPaq
        tipo = self.tipo
        peso = self.peso
        
    
        if not sku or not nombre or not tipo or not peso or not cantxpaq or not codigo_barra:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        
        nomina = self.cargar_datos_nomina()
        
        # Verificar si el producto ya está en la nómina
        for articulo in nomina:
            if articulo['codigo_barra'] == codigo_barra:
                messagebox.showerror("Error", "El producto con este código de barras ya está en la nómina.")
                return

        nuevo_articulo = {
            "sku": sku,
            "nombre": nombre,
            "peso": peso,
            "codigo_barra": codigo_barra,
            "tipo": tipo,
            "cantidadxPaq": cantxpaq
        }

        nomina.append(nuevo_articulo)

        self.grabar_nomina(nomina)

        messagebox.showinfo("Éxito", "Artículo agregado a la nómina.")
        return True
    

    # Metodo que graba la nomina en un archivo json
    @staticmethod
    def grabar_nomina(nomina):
        with open('nomina.json', 'w') as file:
            json.dump(nomina, file, indent=4)
    
    
    
    # Metodo que verifica el codigo de barras, es estatico para no instanciar una clase
    @staticmethod
    def verificar_codigo_barras(codigo_barras):
        if not codigo_barras:
            messagebox.showerror("Error", "El campo de código de barras no puede estar vacío.")
            return

        # Cargar los artículos desde el archivo nomina.json
        nomina = Producto.cargar_datos_nomina()

        # Verificar si el código de barras está cargado
        for idx, item in enumerate(nomina):
            if item['codigo_barra'] == codigo_barras:
                messagebox.showinfo("Resultado", f"El código de barras {codigo_barras} está cargado en el ítem {idx + 1}:\n\n {item['nombre']}")
                return

        messagebox.showinfo("Resultado", f"El código de barras {codigo_barras} no está cargado en la nómina.")
        
        
    @staticmethod
    def eliminar_articulo():
        itemABorrar = simpledialog.askstring("Eliminar artículo", "Ingrese el Codigo de barras que desea eliminar:")
        nomina = Producto.cargar_datos_nomina()
        
        if not itemABorrar:
            messagebox.showerror("Error", "El campo de código de barras no puede estar vacío.")
            return
        
        respuesta = None
        for idx, articulo in enumerate(nomina):
            
            if articulo['codigo_barra'] == itemABorrar:
                respuesta = messagebox.askyesno("Eliminar artículo", f"¿Está seguro que desea eliminar el artículo {articulo['nombre']} de la nómina?")
                if(respuesta):
                    del nomina[idx]
                    Producto.grabar_nomina(nomina)
                    messagebox.showinfo("Éxito", "Artículo eliminado de la nómina.")
                    return
                else:
                    messagebox.showinfo("Cancelado", "La eliminación ha sido cancelada.")
                    return
            
        if not respuesta:
            messagebox.showerror("Error", "El artículo no se encuentra en la nómina.")
            return
        