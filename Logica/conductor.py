from .persona import Persona
class Conductor(Persona):
    def __init__(self, nombre, telefono, correo, cedula, genero):
        super().__init__(nombre, telefono, correo)
        self.cedula = cedula
        self.genero = genero
    def info(self):
        return f"{super().info()}, Cédula: {self.cedula}, Género: {self.genero}"