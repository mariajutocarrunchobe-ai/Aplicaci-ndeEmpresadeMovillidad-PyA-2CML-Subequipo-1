class Persona:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        
    def info(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Correo: {self.correo}"