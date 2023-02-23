# 1. importar la clase
from Personaje import *

# 2. Solicitar atributos para el objetos
print(" ")
print("### Solicitud de datos del heroe ###")
espH = input("Escribe la especie del heroe: ")
nomH = input("Escribe el nombre del heroe: ")
altH = float(input("Escribe la altura del heroe: "))
cargaH = int(input("Escribe cuantas balas se recargaran: "))

print(" ")
print("### Solicitud de datos del villano ###")
espV = input("Escribe la especie del villano: ")
nomV = input("Escribe el nombre del villano: ")
altV = float(input("Escribe la altura del villano: "))
cargaV = int(input("Escribe cuantas balas se recargaran: "))

# 3. Crear los 2 objetos
Heroe = Personaje(espH,nomH,altH)
Villano = Personaje(espV, nomV, altV)

# 4. Acceder a sus atributos y metodos de cada objeto

print(" ")
print("## ATRIBUTOS Y METODOS DEL HEROE ##")
print("El personaje pertenece a la raza: "+ Heroe.especie)
print("El personaje se llama: " + Heroe.nombre)
print("El personaje mide: "+ str(Heroe.altura) + " metros.")
print(" ")

print("METODOS PERSONAJE")
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.RecargarArma(cargaH)

print(" ")
print("## ATRIBUTOS Y METODOS DEL VILLANO ##")
print("El personaje pertenece a la raza: "+ Villano.especie)
print("El personaje se llama: " + Villano.nombre)
print("El personaje mide: "+ str(Villano.altura) + " metros.")
print(" ")

print("METODOS PERSONAJE")
Villano.correr(True)
Villano.lanzarGranada()
Villano.RecargarArma(cargaV)