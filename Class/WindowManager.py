import tkinter as tk
from Class.GUI.VentanaMenuPrincipal import VentanaMenuPrincipal
from Class.GUI.VentanaVerificarCBarras import VentanaVerificarCBarras
from Class.GUI.VentanaAgregarArticulo import VentanaAgregarArticulo
from Class.GUI.VentanaCargarLote import VentanaCargarLote
from Class.GUI.VentanaDatosProcesados import VentanaDatosProcesados

class WindowManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Ocultar la ventana principal
        self.root.protocol("WM_DELETE_WINDOW", self.close_application)  # Protocolo de cierre
        self.current_window = None

    def show_menu_principal(self):
        self._destroy_current_window()
        self.current_window = VentanaMenuPrincipal(tk.Toplevel(), self)
        self.current_window.root.protocol("WM_DELETE_WINDOW", self.close_application)  # Protocolo de cierre
        self.current_window.mostrar()

    def show_verificar_cbarras(self):
        self._destroy_current_window()
        self.current_window = VentanaVerificarCBarras(tk.Toplevel(), self)
        self.current_window.root.protocol("WM_DELETE_WINDOW", self.close_application)  # Protocolo de cierre
        self.current_window.mostrar()

    def show_agregar_articulo(self):
        self._destroy_current_window()
        self.current_window = VentanaAgregarArticulo(tk.Toplevel(), self)
        self.current_window.root.protocol("WM_DELETE_WINDOW", self.close_application)  # Protocolo de cierre
        self.current_window.mostrar()

    def show_cargar_lote(self):
        self._destroy_current_window()
        self.current_window = VentanaCargarLote(tk.Toplevel(), self)
        self.current_window.root.protocol("WM_DELETE_WINDOW", self.close_application)  # Protocolo de cierre
        self.current_window.mostrar()
        
    def show_datos_procesados(self, numero_lote, productos, apellido):
        self._destroy_current_window()
        self.current_window = VentanaDatosProcesados(tk.Toplevel(), self, numero_lote, productos, apellido)
        self.current_window.root.protocol("WM_DELETE_WINDOW", self.close_application)

    def _destroy_current_window(self):
        if self.current_window is not None:
            self.current_window.root.destroy()
            self.current_window = None

    def close_application(self):
        self._destroy_current_window()
        self.root.destroy()

