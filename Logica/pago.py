class Pago:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        
    def procesar(self):
        raise NotImplementedError("Subclase debe implementar procesar()")
class PagoTarjeta(Pago):
    def __init__(self, cantidad, nombre):
        super().__init__(cantidad)
        self.nombre = nombre
class PagoEfectivo(Pago):
    def __init__(self, cantidad, nombre):
        super().__init__(cantidad)
        self.nombre = nombre
    def procesar(self):
        return f"Procesando pago en efectivo de {self.cantidad} para {self.nombre}"