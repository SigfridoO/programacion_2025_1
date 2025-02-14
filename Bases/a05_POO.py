
class Motor:
    def __init__(self, cilindraje:float, numero_serie:str):
        self.cilindraje = cilindraje
        self.numero_serie = numero_serie
    
    def __str__(self):
        return f"Numero de serie: {self.numero_serie}"

class Rueda:
    def __init__(self, rin:int):
        self.rin = rin

    def __str__(self):
        return f"Rueda con rin: {self.rin}"

class Auto:
    def __init__(self, color, numero_p, marca:str, modelo):
        self.color:str = color
        self.numero_puertas:int =numero_p
        self.marca:str = marca
        self.modelo:int = modelo
        self.motor:Motor = None
        self.ruedas = list()
        print("Creando el auto")

    def establecer_motor(self, motor:Motor):
        self.motor = motor
    
    def agregar_rueda(self, rueda:Rueda):
        self.ruedas.append(rueda)

    def mostrar_especificaciones(self):
        print(self)
        print(f"puertas: {self.numero_puertas}, color: {self.color}")
        print(f"motor: {self.motor}")
        print("Ruedas")
        for indice, rueda in enumerate(self.ruedas):
            print(indice + 1, rueda)

    def __str__(self):
        return f"{self.marca} - {str(self.modelo)}"

def main():
    mi_auto = Auto("rojo", 2, "Laborghinni", 2022)

    motor = Motor(12, 'ASDFEWRFDS334A')
    mi_auto.establecer_motor(motor)

    mi_auto.agregar_rueda( Rueda(17) )
    mi_auto.agregar_rueda( Rueda(17) )
    mi_auto.agregar_rueda( Rueda(17) )
    mi_auto.agregar_rueda( Rueda(17) )

    print(mi_auto)
    mi_auto.mostrar_especificaciones()
    
if __name__== "__main__":
    main()