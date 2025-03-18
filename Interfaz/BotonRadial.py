from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QRadioButton, QWidget, QVBoxLayout

import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.boton_rojo = QRadioButton("rojo")
        self.boton_amarillo = QRadioButton("amarillo")
        self.boton_verde = QRadioButton("verde")

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)

        layout.addWidget(self.boton_rojo)
        layout.addWidget(self.boton_amarillo)
        layout.addWidget(self.boton_verde)

        self.boton_rojo.toggled.connect(self.estado_cambiado)
        self.boton_amarillo.toggled.connect(self.estado_cambiado)
        self.boton_verde.toggled.connect(self.estado_cambiado)

        self.setCentralWidget(widget)


    def estado_cambiado(self, valor):
        boton:QRadioButton = self.sender()
        if boton.isChecked():    
            print (valor, boton.text())


def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()