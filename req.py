"""
import requests
from pprint import pprint
API_KEY = "595695c3"
URL = "http://www.omdbapi.com/?apikey="
titulo = "The Matrix"
busqueda = URL + API_KEY + "&t=" + titulo
#print (busqueda)
respuesta_http = requests.get (busqueda)
dic_peli = respuesta_http.json()
#pprint (dic_peli)
print(dic_peli["Year"])

#consultar el API de OMDB y obtener el nombre del director de Fight Club

import requests
from pprint import pprint
API_KEY = "595695c3"
URL = "http://www.omdbapi.com/?apikey="
titulo = "Fight Club"
busqueda = URL + API_KEY + "&t=" + titulo
#print (busqueda)
respuesta_http = requests.get (busqueda)
dic_peli = respuesta_http.json()
#pprint (dic_peli)
pprint(dic_peli["Director"])
pprint(dic_peli["Actors"])
"""

import requests
from pprint import pprint
def datos_peli (nombre_peli):
    API_KEY = "595695c3"
    URL = "http://www.omdbapi.com/?apikey="
    titulo = "Fight Club"
    busqueda = URL + API_KEY + "&t=" + titulo
    #print (busqueda)
    respuesta_http = requests.get (busqueda)
    dic_peli = respuesta_http.json()
    pprint (dic_peli)
    pprint(dic_peli["Director"])
datos_peli("Fight Club")