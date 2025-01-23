import tkinter as tk
import auxiliares as aux

class Ventana:
    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(aux.obtener_res(self.root))
        self.root.state('zoomed')  # para que arranque maximizado
        self.crear_widgets()

    def crear_widgets(self):
        pass

    def mostrar(self):
        self.root.mainloop()

    