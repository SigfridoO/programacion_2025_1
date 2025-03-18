from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QFileDialog, QInputDialog, QColorDialog, QFontDialog, QPushButton
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.boton = QPushButton("Presioname")
        self.boton.clicked.connect(self.mostrar_dialogo)

        self.setCentralWidget(self.boton)

    def mostrar_dialogo(self):
        print("Se mostrará el dialogo")
        # archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", ".")
        # archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", ".")
        # print(archivo)

        # valor, confirmado  = QInputDialog.getText(self, "Se leera texto", 
        #                                           "texto" )
        
        # valor, confirmado  = QInputDialog.getInt(self, "Se leera un entero", 
        #                                           "texto" )
        
        # valor, confirmado  = QInputDialog.getDouble(self, "Se leera un flotante", 
        #                                           "texto" )
        
        # valor, confirmado  = QInputDialog.getItem(self, "Se leera un elemento", 
        #         "colores", ["rojo", "verde", "azul"], editable=False )
        # print(valor, confirmado)

        # fuente, confirmado = QFontDialog.getFont(self)
        # if confirmado:
        #     self.boton.setFont(fuente)

        color = QColorDialog.getColor()
        if color.isValid():
            self.boton.setStyleSheet(f"background-color: {color.name()}")

def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()