from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QTabWidget

import sys

from LayoutsBasicos import Caja

# from ..Bases.a02_Utils import nuevo_tema

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        contenedor = QTabWidget()

        caja1 = Caja("green")
        caja2 = Caja("yellow")
        caja3 = Caja("red")

        contenedor.addTab(caja1, "verde")
        contenedor.addTab(caja2, "amarillo")
        contenedor.addTab(caja3, "rojo")
        contenedor.setTabPosition(QTabWidget.TabPosition.West)
        contenedor.setMovable(True)

        # nuevo_tema("hola")

        self.setCentralWidget(contenedor)


def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()