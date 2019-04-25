#from random import randint
#Sorteo para 5 personas
#parti = ["pepito", "nemo', "rodi", "dino", "grshits"]
#print (parti[randint(0,4)])

#Sorteo para 5 personas, hay 3 premios
#ojo: una persona no puede ganar 2 veces

from random import randint
parti = ["pepito", "nemo", "rodi", "dino", "grshits"]
contador = 4
for sorteo in  range (3):
    un_random = randint (0,contador)
    contador = contador - 1
    ganador = parti[un_random]
    parti.pop(un_random)
    print ("sorteo",sorteo + 1, ":", ganador)


