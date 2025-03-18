from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        boton = QPushButton("Presioname")
        # boton.clicked.connect(self.boton_clickeado)
        # boton.pressed.connect(self.boton_presionado)
        # boton.released.connect(self.boton_liberado)
        boton.setCheckable(True)
        boton.clicked.connect(self.boton_con_estado)
       

        self.setCentralWidget(boton)
        self.setWindowTitle("Botones")
        #self.resize(300, 250)
        #self.setMinimumSize(200, 150)
        #self.setMaximumSize(500, 350)
        self.setFixedSize(400, 200)

        print('Dentro del constructor ventana')

    def boton_presionado(self):
        print ('Se ha presionado el boton')

    def boton_liberado(self):
        print ('Se ha liberado el boton')

    def boton_clickeado(self):
        print ('Se ha clikeado el boton')

    def boton_con_estado(self, valor):
        print(valor)

def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__== '__main__':
    main()