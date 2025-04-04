from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QLabel, QWidget, QPushButton, \
    QGridLayout, QHBoxLayout, QVBoxLayout

from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal as Signal, \
    QObject, Qt

import sys




class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")

class WorkerSignals(QObject):
    luz_roja = Signal(bool)
    luz_amarilla = Signal(bool)
    luz_verde = Signal(bool)

    def __init__(self ):
        super().__init__()

class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()

    def prender_luz_roja(self, estado:bool = False):
        try:
            self.signals.luz_roja.emit(estado)
        except Exception as e:
            print ("Se obtuvo un error al emitir la señal ")

    def prender_luz_amarilla(self, estado:bool = False):
        try:
            self.signals.luz_amarilla.emit(estado)
        except Exception as e:
            print ("Se obtuvo un error al emitir la señal ")

    def prender_luz_verde(self, estado:bool = False):
        try:
            self.signals.luz_verde.emit(estado)
        except Exception as e:
            print ("Se obtuvo un error al emitir la señal ")

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        
        contenedor0 = QGridLayout()

        widget = QWidget()
        widget.setLayout(contenedor0)
        self.setCentralWidget(widget)

        caja0 = Caja('red')
        caja1 = Caja('green')
        caja2 = Caja('yellow')

        layout_vertical1 = QVBoxLayout()
        self.indicador_rojo = self.crear_indicador('red')
        self.indicador_amarillo = self.crear_indicador('yellow')
        self.indicador_verde = self.crear_indicador('green')

        layout_vertical1.addWidget(self.indicador_rojo)
        layout_vertical1.addWidget(self.indicador_amarillo)
        layout_vertical1.addWidget(self.indicador_verde)

        # Para los botones de activación
        layout_horizontal1 = QHBoxLayout()
        self.boton_de_arranque = QPushButton("Iniciar")
        self.boton_de_paro = QPushButton("Detener")

        layout_horizontal1.addWidget(self.boton_de_arranque)
        layout_horizontal1.addWidget(self.boton_de_paro)

        contenedor0.addLayout(layout_vertical1, 0, 0)
        contenedor0.addLayout(layout_horizontal1, 0, 1)
        contenedor0.addWidget(caja2, 1, 0, 1, 2)

        self.setWindowTitle("Semaforo")
        self.resize(350, 250)

        # Enlazando con el worker 
        self.threadPool = QThreadPool()
        self.worker = Worker()
        self.worker.signals.luz_roja.connect(self.cambiar_indicador_rojo)
        self.worker.signals.luz_amarilla.connect(self.cambiar_indicador_amarillo)
        self.worker.signals.luz_verde.connect(self.cambiar_indicador_verde)

        # Creando referencia al control
        self.semaforo = None
        self.boton_de_arranque.setCheckable(True)
        self.boton_de_paro.setCheckable(True)
        self.boton_de_arranque.clicked.connect(self.establecer_senal_arranque)
        self.boton_de_paro.clicked.connect(self.establecer_senal_paro)

    def establecer_senal_arranque(self, valor):
        if self.semaforo:
            self.semaforo.cambiar_estado_bandera(0, valor)

    def establecer_senal_paro(self, valor):
        if self.semaforo:
            self.semaforo.cambiar_estado_bandera(1, valor)



    def establecer_semaforo(self, semaforo):
        self.semaforo = semaforo

    def cambiar_indicador_rojo(self, estado:bool):
        if estado:
            self.modificar_indicador(self.indicador_rojo, 'red')
        else:
            self.modificar_indicador(self.indicador_rojo,'gray')

    def cambiar_indicador_amarillo(self, estado:bool):
        if estado:
            self.modificar_indicador(self.indicador_amarillo, 'yellow')
        else:
            self.modificar_indicador(self.indicador_amarillo,'gray')

    def cambiar_indicador_verde(self, estado:bool):
        if estado:
            self.modificar_indicador(self.indicador_verde, 'green')
        else:
            self.modificar_indicador(self.indicador_verde,'gray')

    def modificar_indicador(self, indicador, color):
        indicador.setStyleSheet(f"""
                background-color: {color};
                border-radius: 30
            """)

    def crear_indicador(self, color:str ="gray"):
        mi_caja = QLabel()
        mi_caja.setStyleSheet(f"""
                background-color: {color};
                border-radius: 30
            """)
        mi_caja.setFixedSize(60, 60)

        return mi_caja

    def obtener_worker(self):
        return self.worker

    def closeEvent(self, a0):
        
        print('Se presiono el boton cerrar')
        if self.semaforo:
            self.semaforo.detener()
        
        

def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()