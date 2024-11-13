import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import json  # Importar el módulo para manejar JSON

from interfaces.ui_distribucion import Ui_MainWindow

class DistrubutionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Distribución de Plantas")  # Establece el título de la ventana
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint)  # Deshabilita el botón de maximizar
        
    def abrir_ventana_Menu(self):
        from .menu import MenuWindow  # Importamos la ventana de gestión#+
        # Capturamos la posición de la ventana actual antes de cerrarla
        pos_x = self.geometry().x()
        pos_y = self.geometry().y()
        self.ventana_Menu = MenuWindow()
        # Establecemos la misma posición para la nueva ventana
        self.ventana_Menu.move(pos_x, pos_y)
        self.ventana_Menu.show()
        self.close()  # Cerramos la ventana de menú