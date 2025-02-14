from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        boton = QPushButton("Presioname")

        self.setCentralWidget(boton)
        self.setWindowTitle("Botones")
        #self.resize(300, 250)
        #self.setMinimumSize(200, 150)
        #self.setMaximumSize(500, 350)
        self.setFixedSize(400, 200)

        print('Dentro del constructor ventana')

def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

if __name__== '__main__':
    main()