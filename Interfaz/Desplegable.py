from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QComboBox
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        desplegable = QComboBox()
        desplegable.addItems(['opción 1', 'opción 2', 'opción 3', 'opción 4'])

        desplegable.currentIndexChanged.connect(self.indice_cambiado)
        desplegable.currentTextChanged.connect(self.texto_selecionado)

        self.setCentralWidget(desplegable)


    def indice_cambiado(self, indice):
        print(f"El indice seleccionado es {indice}")

    def texto_selecionado (self, texto):
        print(f"El texto seleccionado es {texto}")


def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()