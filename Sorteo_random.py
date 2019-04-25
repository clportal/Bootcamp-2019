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

##### teniendo una lista hecha puedes utilizar esta funcion definir numero de premios y realizar el sorteo  
def sorteos(cantidad_premios,lista):
    if cantidad_premios <= len(lista):
        sorteo=1
        while sorteo<=cantidad_premios:
            x=len(lista)-1
            y=randint(0,x)
            z= lista[y]
            print("el ganador numero",sorteo,"es",z)
            lista.pop(y)
            sorteo=sorteo+1
    else:
        print("tu numero de premios supera al de participantes... dejate de joder")
