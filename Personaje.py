
class Personaje:
    #Creamos el constructor
    def __init__(self, esp, nom, alt): 
        #atributos del personaje
        self.especie = esp
        self.nombre = nom
        self.altura = alt
    
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
        print("El arma tiene ahora: "+ str(cargador) + " balas.")