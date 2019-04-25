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
#yo = Persona ("fulano", 400, "30 de julio")

# modificar la clase persona, agregarle un atributo edad y 
# un metodo cumple_anhos, y un metodo get_edad
# inicializa / crear un objeto de tipo Persona y hacerle cumplir anhos

    def get_edad (self):
        return self.edad
    def set_edad (self, cantidad):
        self.edad = cantidad - 1
yo = Persona ("fulano", 400, "30 de julio")
#yo.get_edad()
#yo.set_edad(23)
#yo.get_edad()