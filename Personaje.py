
class Personaje:
    #atributos del personaje
    especie = "Humano"
    nombre = "Jefe Maestro"
    altura = 2.18
    
#Metodos del personaje

def correr(self, status):
    if(status):
        print("El personaje "+ self.nombre + " esta corriendo.")
    else:
        print("El personaje " + self.nombre + " se detuvo.")
        
def lanzarGranada(self):
    print("Se lanzó granada.")
    
def RecargarArma(self, municiones):
    cargador = 5
    cargador = cargador + municiones
    print("El arma tiene ahora: "+ cargador + " balas.")