class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if (color == "rojo"):
            self.color = color
        elif(color == "verde"):
            self.color = color
        elif(color == "amarillo"):
            self.color = color
        elif(color == "negro"):
            self.color = color
        elif(color == "blanco"):
            self.color = color
    
class Auto:
    cantidadCreados = None
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        
    def cantidadAsientos(self):
        lista = []
        for i in self.asientos:
            verificar = str(type(i))
            if verificar[8] == "_":
                lista.append(1)
        return sum(lista)

    def verificarIntegridad(self):
        for i in self.asientos:
            if i.registro == self.registro and self.registro == Motor.cambiarRegistro:
                return "Auto original"
            else:
                return "Las piezas no son originales"


class Motor:
    def __init__(self, numerosCilindros, tipo, registro):
        self.numerosCilindros = numerosCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if( tipo == "electrico"):
            self.tipo = tipo
        elif( tipo == "gasolina"):
            self.tipo = tipo