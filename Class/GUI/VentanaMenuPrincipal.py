from .Ventana import Ventana
import tkinter as tk

class VentanaMenuPrincipal(Ventana):
    def __init__(self, root, window_manager):
        super().__init__(root, window_manager, title="Menú Principal")

    def crear_widgets(self):
        menu_frame = tk.Frame(self.root)
        menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        btn_cargar_lote = tk.Button(menu_frame, text="Cargar lote", command=self.cargar_lote, width=25, height=3, font=("Arial", 16))
        btn_cargar_lote.pack(pady=10)

        btn_verificar_sku = tk.Button(menu_frame, text="Comprobar código de Barras", command=self.verificar_sku, width=25, height=3, font=("Arial", 16))
        btn_verificar_sku.pack(pady=10)

    def cargar_lote(self):
        self.window_manager.show_cargar_lote()

    def verificar_sku(self):
        self.window_manager.show_verificar_cbarras()