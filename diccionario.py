diccionario {} #diccionario vacio
nombre_de_diccionaio = {"nombre_clave":"valor"}
#lista
personalist = ["marce",32,"programador"] #lista
#diccionario
dic_persona = {"nombre": "marce","edad":32} #diccionario
print (dic_persona)
dic_persona["edad"] = "mm cuanto me pones"
personalist[1] = "mm cuanto me pones"
print(dic_persona["edad"])
print (personalist[1])
dic_persona ["profesion"] = "programador"
print (dic_persona)
print (dic_persona["profesion"])
print (dic_persona["estatura"]) #error
#esta = dic_persona["estatura"]
print (dic_persona.get("estatura"))
dic_persona["estatura"] = 1.85
if dic_persona.get ("estatura")!=None:
    print ("si esxite la clave estaturaelse")
else:
    print ("no existe la clave estatura")
print (dic_persona)
dic_persona2 = {"nombre":"mace","edad":32,"peinado":"algo"}
print(dic_persona2)
