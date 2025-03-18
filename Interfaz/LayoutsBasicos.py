from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel , \
    QHBoxLayout, QVBoxLayout, QWidget
import sys

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        
        caja1 = Caja("#3454F3")
        caja2 = Caja("magenta")
        caja3 = Caja("yellow")
        caja4 = Caja("green")

        layout.addWidget(caja1)
        layout.addWidget(caja2)
        layout.addWidget(caja3)
        layout.addWidget(caja4)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()