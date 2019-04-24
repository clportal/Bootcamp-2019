# en el archivo persona.py crear una clase Persona con atributo nombre
#despues instanciar eun objeto de tipo persona

class Persona:
    nombre = None
    edad = None
    cumpleanhos = None
    def __init__ (self, el_nombre, la_edad ,el_cumpleanhos):
        self.nombre = el_nombre
        self.edad = la_edad
        self.cumpleanhos = el_cumpleanhos
        print ("hola me llamo", self.nombre, "tengo", self.edad,"anhos", "mi cumpleanhos es en", self.cumpleanhos)
yo = Persona ("fulano", 400, "30 de julio")

