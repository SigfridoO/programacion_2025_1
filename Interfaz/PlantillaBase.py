from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

def main():
    print('Dentro de main')
    app = QApplication(sys.argv) 
    ventana = QMainWindow()
    ventana.show()
    sys.exit(app.exec())
    
if __name__== '__main__':
    main()