from .Ventana import Ventana
from .VentanaCargarLote import VentanaCargarLote
import tkinter as tk

class VentanaMenuPrincipal(Ventana):
    def __init__(self):
        super().__init__(title="Menu Principal")

    def crear_widgets(self):
        menu_frame = tk.Frame(self.root)
        menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        btn_cargar_lote = tk.Button(menu_frame, text="Cargar lote", command=self.cargar_lote, width=20, height=3, font=("Arial", 16))
        btn_cargar_lote.pack(pady=10)

        btn_verificar_sku = tk.Button(menu_frame, text="Ver SKU", command=self.verificar_sku, width=20, height=3, font=("Arial", 16))
        btn_verificar_sku.pack(pady=10)

    def cargar_lote(self):
        ventana_cargar_lote = VentanaCargarLote()
        self.root.destroy()
        ventana_cargar_lote.mostrar()

    def verificar_sku(self):
        print("Verificar SKU")