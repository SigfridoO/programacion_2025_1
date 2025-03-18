from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QLabel, QWidget, QPushButton, QCheckBox, QSpinBox, \
    QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        layout_vertical_1 = QVBoxLayout()

        caja1 = Caja("red")
        caja2 = Caja("cyan")
        caja3 = Caja("orange")

        texto_titulo = QLabel("Proyecto")
        fuente = QFont("Manjari", 18)
        texto_titulo.setFont(fuente)
        texto_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Para los elementos centrales
        layout_vertical_2 = QVBoxLayout()
        layout_horizontal_2 = QHBoxLayout()

        layout_vertical_2.addLayout(layout_horizontal_2)
        checkbox_activar = QCheckBox("Activar")
        etiqueta_temperatura = QLabel("Temperatura")
        spin_temperatura = QSpinBox()

        layout_horizontal_2.addWidget(checkbox_activar)
        layout_horizontal_2.addWidget(etiqueta_temperatura)
        layout_horizontal_2.addWidget(spin_temperatura)

        # Para los elementos inferiores
        layout_horizontal_1 = QHBoxLayout()

        layout_vertical_1.addWidget(texto_titulo)
        layout_vertical_1.addLayout(layout_vertical_2)
        layout_vertical_1.addLayout(layout_horizontal_1)

        boton_aceptar = QPushButton("Aceptar")
        boton_cancelar = QPushButton("Cancelar")
        boton_aplicar = QPushButton("Aplicar")

        layout_horizontal_1.addWidget(boton_aceptar)
        layout_horizontal_1.addWidget(boton_cancelar)
        layout_horizontal_1.addWidget(boton_aplicar)
        


        widget = QWidget()
        widget.setLayout(layout_vertical_1)

        self.setCentralWidget(widget)



def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()