from PyQt6.QtWidgets import QApplication, QMainWindow, QStatusBar
    
from PyQt6.QtGui import QAction, QIcon
import sys

from Etiquetas import abs_path

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStatusBar(QStatusBar())
        menu = self.menuBar()
        menu_archivo = menu.addMenu("Archivo")
        menu_archivo.addAction("Abrir")
        # print (abs_path("pato.jpg"))

        menu_archivo.addAction(
            QIcon(abs_path("pato.jpg")), 
            "Salir", 
            "Ctrl+Q", 
            self.close)
        
        accion_mostrar = QAction("Mostrar", self)
        accion_mostrar.setShortcut("Ctrl+F")
        accion_mostrar.setIcon(QIcon(abs_path("pato.jpg")))
        accion_mostrar.triggered.connect(self.mi_funcion_superimportante)
        accion_mostrar.setStatusTip("Comando importate")

        menu_editar = menu.addMenu("Editar")
        menu_editar.addAction(accion_mostrar) 
        menu_ayuda = menu.addMenu("Ayuda")
        self.resize(400, 350)

    def mi_funcion_superimportante(self):
        print ("Se esta realizando una accción superimportate")


def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()