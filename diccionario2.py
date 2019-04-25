#crear un diccionario persona con claves nombre edad estatura 
# e imprimir cada uno de los valores de las claves en un print diferente
#luego cambiar la edad__ con un input()__a otro valor e imprimir de nuevo
#luego agregar un par clave "hobbie" que contenga una *lista* de hobbies 
# e imprimir todo el diccionario
dic_persona3 = {"nombre":"claudia","edad":30,"estatura":"1.69"}
print(dic_persona3.get("nombre"))
print(dic_persona3.get("edad"))
print(dic_persona3.get("estatura"))

#####segundA PARTE
buscar = input ("que edad tiene")
dic_persona3 ["edad"] = buscar
print (dic_persona3.get("edad"))

#parte 3
pasatiempos = ["escuchar musica","ver peliculas","ver series"]
dic_persona3 ["hobbies"] = pasatiempos
print (dic_persona3)
