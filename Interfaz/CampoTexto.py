from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.campo_texto = QLineEdit()
        self.campo_texto.textChanged.connect(self.texto_cambiado)
        self.campo_texto.returnPressed.connect(self.enter_presionado)
        self.setCentralWidget(self.campo_texto)
        self.resize(400, 100)

    def texto_cambiado(self, texto):
        print(texto)
    
    def enter_presionado(self):
        contenido = self.campo_texto.text()
        self.setWindowTitle(contenido)
def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()