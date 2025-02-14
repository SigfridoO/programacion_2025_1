from a02_Utils import nuevo_subtema

class Persona:
    # constructor
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = None
        self.altura = None
        self.color_de_ojos = ""

    def saludar(self):
        print (f"¡Hola <3!, mi nombre es {self.__nombre} {self.apellido} ¿Como estas?")

    def ir_a_cenar(self, con_quien):
        print(f'¡Hola: {con_quien}! Me invitas a cenar esta noche')
    
    def establecer_altura(self, valor):
        self.altura = valor
        
    
    def establecer_ojos(self, color:str):
        self.color_de_ojos = color

    # metodo toStr (representación en cadena de caracteres del objeto)
    def __str__(self):
        pass

daniela = Persona("Daniela", "De Miranda")
daniela.establecer_altura(1.76)
daniela.establecer_ojos("Miel")
daniela.saludar()
daniela.ir_a_cenar("Justin")

nuevo_subtema("Ahora con Victor")
amayrani = Persona("Amayrani", "Fuentes") 
amayrani.ir_a_cenar("Victor")
print(amayrani.apellido)
# print(amayrani.__nombre)
