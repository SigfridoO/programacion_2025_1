from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QStackedLayout, QWidget
import sys
from PyQt6.QtCore import Qt

from LayoutsBasicos import Caja

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout:QStackedLayout = QStackedLayout()

        widget = QWidget()
        widget.setLayout(self.layout)

        caja1 = Caja('red')
        caja2 = Caja('green')
        caja3 = Caja('blue')
        caja4 = Caja('pink')

        self.layout.addWidget(caja1)
        self.layout.addWidget(caja2)
        self.layout.addWidget(caja3)
        self.layout.addWidget(caja4)


        self.layout.setCurrentIndex(2)

        self.setCentralWidget(widget)

        self.resize(400, 250)

    def keyPressEvent(self, event):
        # print(event.key())
        indice = self.layout.currentIndex()
        indice_maximo = self.layout.count() -1

        print("indice: " , indice)
        print("indice maximo: ", indice_maximo)

        if event.key() == Qt.Key.Key_Left:
            # print ("Se oprimio la flecha izquierda")
            indice = indice - 1

        if event.key() == Qt.Key.Key_Right:
            print("Se oprimio la flecha derecha")
            indice += 1

        if indice > indice_maximo:
            indice = 0
        if indice < 0:
            indice = indice_maximo

        self.layout.setCurrentIndex(indice)

        event.accept()



def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()