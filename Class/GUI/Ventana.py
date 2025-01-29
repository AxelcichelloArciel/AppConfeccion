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
    
    def valida_texto(self, texto):
        return texto.isalpha() or texto == ''
    
    def valida_numero(self, texto, longitud = None):
        if longitud is not None:
            return texto.isdigit() and len(texto) <= longitud or texto == ""
        return texto.isdigit() or texto == ''
    
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