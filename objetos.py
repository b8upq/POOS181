# 1. importar la clase
from Personaje import *

# 2. Istanciar un objeto
Heroe = Personaje()

# 3. Acceder a sus atributos
print("ATRIBUTOS PERSONAJE")
print("El personaje pertenece a la raza: "+ Heroe.especie)
print("El personaje se llama: " + Heroe.nombre)
print("El personaje mide: "+ str(Heroe.altura) + " metros.")
print(" ")

print("METODOS PERSONAJE")
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.RecargarArma(45)