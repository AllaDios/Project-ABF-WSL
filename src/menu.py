import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

from interfaces.ui_menu import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Menu de Plantas")  # Establece el título de la ventana
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint)  # Deshabilita el botón de maximizar
        
        # Conectamos el botón (asumiendo que se llama pushButton_gestion) con la función que abre la ventana de gestión
        self.pushButton_3.clicked.connect(self.abrir_ventana_gestion)

    def abrir_ventana_gestion(self):
        from .gestionar import MainWindow as GestionWindow  # Importamos la ventana de gestión#+
        self.ventana_gestion = GestionWindow()
        self.ventana_gestion.show()
        self.close()  # Cerramos la ventana de menú
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())