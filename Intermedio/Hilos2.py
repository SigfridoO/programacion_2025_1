import time
import threading

class Programa(threading.Thread):
    def __init__(self, nombre, tiempo):
        super().__init__()
        self.nombre = nombre
        self.tiempo = tiempo
        print(f"Iniciando tarea con el nombre {self.nombre}")

    def run(self):
        print(f"Se iniciara la operación de la tarea {self.nombre}")
        time.sleep(self.tiempo)
        print(f"terminando de la tarea {self.nombre}")

    def mostrar (self):
        print("Mostrando algo")

def main():
    print("dentro de main")
    tarea1 = Programa("Estructura", 5)
    tarea1.start()

    #tareas2 = Programa("Electronica", 8)
    # despulpadora.correr()
    # despulpadora.mostrar()

if __name__=="__main__":
    main()