from classes.classPlantas import Planta

class Vivero:
    def __init__(self, nombre, plantas):
        self.plantas = plantas
        self.nombre = nombre
    
    def agregar_planta(self, planta):
        self.plantas.append(planta)

    def get_plantas(self):
        return self.plantas
        
    def eliminar_planta(self, planta):
        if planta in self.plantas:
            self.plantas.remove(planta)

    def buscar_planta_por_nombre(self, nombre):
        for planta in self.plantas:
            if planta.nombre == nombre:
                return planta
        return None  # Si no se encuentra, devuelve None