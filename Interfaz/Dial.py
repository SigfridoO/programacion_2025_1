from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QDial

import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dial = QDial()
        self.dial.valueChanged.connect(self.valor_cambiado)
        self.dial.setRange(-10, 10)
        self.dial.setWrapping(False)
        
        self.setCentralWidget(self.dial)

    def valor_cambiado(self, valor):
        print(valor)
        if valor < self.dial.minimum():
            self.dial.setValue(self.dial.minimum())

        if valor > self.dial.maximum():
            self.dial.setValue(self.dial.maximum())


def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()