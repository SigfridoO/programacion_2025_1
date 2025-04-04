import threading
import time

from Temporizador import Temporizador
from Interfaz import Worker

class Semaforo():
    def __init__(self):
        print("Dentro de semaforo")
        self.TON_0 = Temporizador("TON_00", 6)
        self.TON_1 = Temporizador("TON_01", 2)
        self.TON_2 = Temporizador("TON_02", 4)

        self.M = []
        for i in range(20):
            self.M.append(False)

        self.M[2] = True

        self.luz_roja = False
        self.luz_amarilla = False
        self.luz_verde = False

        self.funcionando = False

        self.worker:Worker = None

        self.tarea = threading.Thread(target= self.semaforo_funcionando)

    def iniciar(self):
        if self.tarea:
            self.tarea.start()
    def detener(self):
        self.funcionando = False
        
    def semaforo_funcionando(self):
        self.funcionando = True
        while self.funcionando:
            self.M[2]= (self.M[0] or self.M[2]) and not self.M[1]
            
            self.TON_0.entrada = self.M[2] and not self.TON_2.salida
            self.TON_0.actualizar()

            self.TON_1.entrada = self.M[2] and self.TON_0.salida
            self.TON_1.actualizar()

            self.TON_2.entrada = self.M[2] and self.TON_1.salida
            self.TON_2.actualizar()

            self.luz_roja = self.M[2] and not self.TON_0.salida

            self.luz_amarilla = self.M[2] and self.TON_0.salida and not self.TON_1.salida

            self.luz_verde = self.M[2] and self.TON_1.salida

            print(f"R: {self.luz_roja} A: {self.luz_amarilla} V: {self.luz_verde}")

            # Mapeando hacia la interfaz
            if self.worker:
                self.worker.prender_luz_roja(self.luz_roja)
                self.worker.prender_luz_amarilla(self.luz_amarilla)
                self.worker.prender_luz_verde(self.luz_verde)

            time.sleep(0.01)

    def cambiar_estado_bandera(self, numero, estado):
        if numero < len(self.M) and numero >= 0:
            self.M[numero] = estado

    def establecer_worker(self, worker):
        self.worker = worker
    
    def obtener_semaforo(self):
        return self

def main():
    print("Dentro de main")
    semaforo = Semaforo()
    semaforo.iniciar()

if __name__ == "__main__":
    main()