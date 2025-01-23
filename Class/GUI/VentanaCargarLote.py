from .Ventana import Ventana
from ..Producto import Producto
from .VentanaDatosProcesados import VentanaDatosProcesados
import tkinter as tk
from collections import Counter
import json

class VentanaCargarLote(Ventana):
    def __init__(self):
        super().__init__(title="Cargar Lote")

    def crear_widgets(self):
        frame = tk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label_apellido = tk.Label(frame, text="Ingrese su apellido:", font=("Arial", 12))
        label_apellido.pack(pady=10)

        self.entry_apellido = tk.Entry(frame, width=50, font=("Arial", 16))
        self.entry_apellido.pack(pady=10, ipady=10)  # ipady aumenta la altura del campo de entrada

        label_lote = tk.Label(frame, text="Ingrese el número de lote:", font=("Arial", 12))
        label_lote.pack(pady=10)

        self.entry_lote = tk.Entry(frame, width=50, font=("Arial", 16))
        self.entry_lote.pack(pady=10, ipady=10)  # ipady aumenta la altura del campo de entrada
        self.entry_lote.bind("<KeyRelease>", self.validar_entrada_lote) # evento para validar el digito ingresado

        label = tk.Label(frame, text="Ingrese los números de SKU (cadena continua de 13 dígitos cada uno):", font=("Arial", 12))
        label.pack(pady=10)

        # Crear un widget Text con una barra de desplazamiento vertical
        self.text = tk.Text(frame, width=50, height=15, font=("Arial", 16), wrap=tk.WORD)
        self.text.pack(pady=10)

        scrollbar_y = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.text.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.config(yscrollcommand=scrollbar_y.set)

        btn_procesar = tk.Button(frame, text="Procesar lote", command=self.procesar_datos, width=20, height=3, font=("Arial", 16))
        btn_procesar.pack(pady=10)

        # Vincular el evento de teclado para formatear automáticamente cada 13 dígitos y validar la entrada
        self.text.bind("<KeyRelease>", self.formatear_y_validar_texto) # evento para formatear la cadena de entrada

    def validar_entrada_lote(self, event):
        contenido = self.entry_lote.get() # obtiene el contenido del campo de entrada
        if not contenido.isdigit(): # valida si el contenido es un digito
            self.entry_lote.delete(0, tk.END) # si no es un digito borra el contenido
            self.entry_lote.insert(0, ''.join(filter(str.isdigit, contenido))) # inserta solo los digitos en el campo de entrada

    def formatear_y_validar_texto(self, event):
        contenido = self.text.get("1.0", tk.END).replace('\n', '').replace('\r', '').replace(' ', '') # Obtener el contenido del widget Text y eliminar saltos de línea, retornos de carro y espacios en blanco 
        contenido = ''.join(filter(str.isdigit, contenido))  # Eliminar cualquier carácter no numérico
        formateado = '' 
        for i in range(0, len(contenido), 13): # recorre la cadena de entrada de 13 en 13
            formateado += contenido[i:i+13] + '\n' # agrega un salto de linea cada 13 digitos
        self.text.delete("1.0", tk.END) # borra el contenido del widget Text
        self.text.insert("1.0", formateado.strip()) # inserta el contenido formateado en el widget Text

    def procesar_datos(self):
        numero_lote = self.entry_lote.get().strip() # Obtiene el número de lote ingresado
        if not numero_lote: # valida si el número de lote está vacío
            print("Error, el número de lote no puede estar vacío") # imprime un mensaje de error
            return 

        entrada = self.text.get("1.0", tk.END).strip().replace('\n', '').replace('\r', '').replace(' ', '') # Obtiene el contenido del widget Text y elimina saltos de línea, retornos de carro y espacios en blanco
        if len(entrada) % 13 != 0: # valida si la cadena de entrada no es multiplo de 13
            print("Error, la cadena no es multiplo de 13")  # imprime un mensaje de error
            return
        
        numeros = [entrada[i:i+13] for i in range(0, len(entrada), 13)]  # separa la cadena de a conjuntos de 13 digitos (ya que los codigos de barra son conjuntos de 13)
        conteo = Counter(numeros)  # recorre el arreglo de numeros y los agrupa por cada uno de los conjuntos.

        # Cargo los datos de la nomina
        with open('nomina.json', 'r') as file: # Abre el archivo nomina.json en modo lectura
            nomina = json.load(file) # Carga el contenido del archivo en la variable nomina

        # Creo diccionario para buscar rápido por código de barras
        nomina_dict = {item['codigo_barra']: item for item in nomina} # crea un diccionario con el codigo de barras como clave y el item como valor

        productos = [] # crea una lista vacia para almacenar los productos

        for numero, cantidad in conteo.items(): # recorre el diccionario de conteo
            if numero in nomina_dict: # valida si el numero de barras se encuentra en la nomina
                sku = nomina_dict[numero]['codigo'] 
                nombre = nomina_dict[numero]['nombre']
                producto = Producto(codigo=sku, nombre=nombre, codigo_barra=numero, cantidad=cantidad)
                productos.append(producto)
            else:
                print(f"Codigo de barras: {numero} no se encontrado en la nomina")

        # Abrir la nueva ventana con los datos procesados
        ventana_datos_procesados = VentanaDatosProcesados(numero_lote, productos)
        self.root.destroy()  # Destruir la ventana principal
        ventana_datos_procesados.mostrar()
        self.root.quit()  # Detener el bucle principal de la ventana principal