from PyQt6.QtWidgets import QApplication
import sys

from Interfaz import Ventana
from Semaforo import Semaforo

class Inicio(Ventana):
    def __init__(self):
        super().__init__()
        semaforo = Semaforo()
        semaforo.iniciar()
        semaforo.establecer_worker(self.obtener_worker())
        self.establecer_semaforo(semaforo)

def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Inicio()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()