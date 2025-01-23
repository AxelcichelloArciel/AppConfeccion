from .Ventana import Ventana
import tkinter as tk

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
        text_productos = tk.Text(frame, width=80, height=20, font=("Arial", 10), wrap=tk.WORD)
        text_productos.pack(pady=10)

        # Formatear y agregar los productos al widget Text
        for producto in self.productos:
            text_productos.insert(tk.END, f"SKU: {producto.codigo}\n")
            text_productos.insert(tk.END, f"Nombre: {producto.nombre}\n")
            text_productos.insert(tk.END, f"Codigo de Barra: {producto.codigo_barra}\n")
            text_productos.insert(tk.END, f"Tipo: {producto.tipo}\n")
            text_productos.insert(tk.END, f"Cantidad de paquetes: {producto.cantidad}\n")
            text_productos.insert(tk.END, f"Cantidad de unidades: {producto.unidades}\n")
            text_productos.insert(tk.END, "-"*40 + "\n")

        text_productos.config(state=tk.DISABLED)  # Hacer el widget Text de solo lectura

        btn_cerrar = tk.Button(frame, text="Menu Principal", command=self.cerrar_ventana, width=20, height=3, font=("Arial", 16))
        btn_cerrar.pack(pady=10)

        btn_imprimir = tk.Button(frame, text="Imprimir", command=self.imprimir, width=20, height=3, font=("Arial", 16))
        btn_imprimir.pack(pady=10)

    def cerrar_ventana(self):
        self.root.quit()  # Detener el bucle principal
        self.root.destroy()  # Destruir la ventana
        from .VentanaMenuPrincipal import VentanaMenuPrincipal
        ventana_menu_principal = VentanaMenuPrincipal()
        ventana_menu_principal.mostrar()

    def imprimir(self):
        # Aquí puedes agregar la lógica para imprimir
        print("Imprimir datos")