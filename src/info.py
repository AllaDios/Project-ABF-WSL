import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from classes.classPlantas import Planta
from interfaces.ui_info import Ui_MainWindow

class InfoWindow(QMainWindow):
    def __init__(self, planta, vivero):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Información de la Planta")  # Establece el título de la ventana
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint)  # Deshabilita el botón de maximizar

        # Almacenar la planta y el vivero en la instancia
        self.planta = planta
        self.vivero = vivero

        # mostrar información sobre la planta
        self.ui.label_2.setText(str(self.planta.humedad) + "%")
        self.ui.label_3.setText(self.planta.nombre)  
        
    def abrir_ventana_Distribucion(self):
        from .distribucion import DistributionWindow  # Importamos la ventana de gestión

        # Capturamos la posición de la ventana actual antes de cerrarla
        pos_x = self.geometry().x()
        pos_y = self.geometry().y()

        # Pasamos el objeto vivero cuando se abre la ventana de distribución
        self.ventana_Distribucion = DistributionWindow(self.vivero)
        # Establecemos la misma posición para la nueva ventana
        self.ventana_Distribucion.move(pos_x, pos_y)
        self.ventana_Distribucion.show()
        self.close()  # Cerramos la ventana de información

