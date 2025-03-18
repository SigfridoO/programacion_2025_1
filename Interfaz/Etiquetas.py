from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QFont
import sys
from pathlib import Path

def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        etiqueta = QLabel("Saludos")
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter \
            | Qt.AlignmentFlag.AlignBottom)
        fuente = QFont("Manjari", 20)
        etiqueta.setFont(fuente)
        imagen = QPixmap(abs_path("pato.jpg"))
        etiqueta.setPixmap(imagen)
        etiqueta.setScaledContents(True)

        self.setCentralWidget(etiqueta)
        self.setFixedSize(400, 250)

def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()