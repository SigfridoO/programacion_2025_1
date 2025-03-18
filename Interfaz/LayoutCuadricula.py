from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QGridLayout, QWidget
import sys

from LayoutsBasicos import Caja

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        widget = QWidget()
        widget.setLayout(layout)


        caja1 = Caja("#456523")
        caja2 = Caja("#2134CC")
        caja3 = Caja('green')

        layout.addWidget(caja1, 0, 0)
        
        layout.addWidget(caja3, 0, 2, 3, 1)
        layout.addWidget(caja2, 1, 1, 1, 2)
        self.setCentralWidget(widget)

        self.resize(350, 250)


def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()