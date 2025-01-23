class Producto:
    def __init__(self, codigo, nombre, codigo_barra, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.codigo_barra = codigo_barra
        self.tipo = self.obtener_tipo()
        self.cantidad = cantidad
        self.unidades = self.calc_unidades()  # Calcular las unidades al inicializar

    def __repr__(self):
        return f"Producto(codigo={self.codigo}, nombre={self.nombre}, codigo_barra={self.codigo_barra}, tipo={self.tipo}, cantidad={self.cantidad}), unidades={self.unidades}"
    
    def obtener_tipo(self):
        tipo = self.nombre.split()[0].lower()
        tipos_validos = {"toalla", "toallon", "repasador", "alfombra", "tela", "bata"}
        if tipo not in tipos_validos:
            return None
        return tipo
    
    def calc_unidades(self):
        if self.tipo == "toallon":
            return self.cantidad * 6
        elif self.tipo == "toalla":
            return self.cantidad * 12
        elif self.tipo == "repasador":
            return self.cantidad * 24
        else:
            return None  # Dejar en blanco para otros tipos