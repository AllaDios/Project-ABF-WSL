import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

from interfaces.ui_menu import Ui_MainWindow

class MenuWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Menu de Plantas")  # Establece el título de la ventana
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint)  # Deshabilita el botón de maximizar
        
        # Conectamos el botón con la función que abre la ventana de gestión
        self.pushButton_3.clicked.connect(self.abrir_ventana_gestion)

        # Conectamos el botón con la función que abre la ventana de distribucion
        self.pushButton_2.clicked.connect(self.abrir_ventana_distribucion)

    def abrir_ventana_gestion(self):
        from .gestionar import GestionWindow  # Importamos la ventana de gestión#+
        # Capturamos la posición de la ventana actual antes de cerrarla
        pos_x = self.geometry().x()
        pos_y = self.geometry().y()
        self.ventana_gestion = GestionWindow()
        # Establecemos la misma posición para la nueva ventana
        self.ventana_gestion.move(pos_x, pos_y)
        self.ventana_gestion.show()
        self.close()  # Cerramos la ventana de menú

    def abrir_ventana_distribucion(self):
        from .distribucion import DistrubutionWindow  # Importamos la ventana de gestión#+
        # Capturamos la posición de la ventana actual antes de cerrarla
        pos_x = self.geometry().x()
        pos_y = self.geometry().y()
        self.ventana_distribucion = DistrubutionWindow()
        # Establecemos la misma posición para la nueva ventana
        self.ventana_distribucion.move(pos_x, pos_y)
        self.ventana_distribucion.show()
        self.close()  # Cerramos la ventana de menú

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())