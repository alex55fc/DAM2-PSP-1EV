"""Ejercicio 12: Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad 
(puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crea sus métodos get, set y toString. 
Tendrá dos métodos especiales"""
class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad
        pass

    def get_titular(self):
        return self.titular
    
    def set_titular(self, titular):
        self.titular = titular
    
    def get_cantidad(self):
        return self.cantidad
    
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    

    def to_string(self):
        return str(self)
    
    "metodos"
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
            if self.cantidad < 0:
                self.cantidad = 0
    
cuenta1 = Cuenta('Alex')
print(cuenta1.get_titular(), cuenta1.get_cantidad())
cuenta1.ingresar(100)
print(cuenta1.get_titular(), cuenta1.get_cantidad())
cuenta1.ingresar(-200)
print(cuenta1.get_titular(), cuenta1.get_cantidad())
cuenta1.retirar(20)
print(cuenta1.get_titular(), cuenta1.get_cantidad())
