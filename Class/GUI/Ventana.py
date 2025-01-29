import tkinter as tk
import json
import auxiliares as aux
from tkinter import messagebox

class Ventana:
    def __init__(self, root, window_manager, title):
        self.window_manager = window_manager
        self.root = root
        self.root.title(title)
        self.root.geometry(aux.obtener_res(self.root))
        self.root.state('zoomed')  # para que arranque maximizado
        self.crear_widgets()

    def crear_widgets(self):
        pass

    def mostrar(self):
        self.root.mainloop()
        
    def cargar_datos_nomina(self):
        with open('nomina.json', 'r') as file:
            datos_nomina = json.load(file)
            return datos_nomina
            
    def valida_texto(self, texto):
        return texto.isalpha() or texto == ''
    
    def valida_numero(self, texto, longitud = None):
        if longitud is not None:
            return texto.isdigit() and len(texto) <= longitud or texto == ""
        return texto.isdigit() or texto == ''
    
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
        
        nomina = self.cargar_datos_nomina()
        
        # Verificar si el producto ya está en la nómina
        for articulo in nomina:
            if articulo['codigo_barra'] == codigo_barras:
                messagebox.showerror("Error", "El producto con este código de barras ya está en la nómina.")
                return

        nuevo_articulo = {
            "sku": sku,
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

        self.entry_sku.config(validate='key', validatecommand=(self.root.register(self.valida_numero), '%P')) 
        self.entry_peso.config(validate='key', validatecommand=(self.root.register(self.valida_texto), '%P'))
        self.entry_codigo_barras.config(validate='key', validatecommand=(self.root.register(self.valida_numero), '%P'))
        self.entry_cantxpaq.config(validate='key', validatecommand=(self.root.register(self.valida_numero), '%P'))
        self.entry_tipo.config(validate='key', validatecommand=(self.root.register(self.valida_texto), '%P'))