import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from classes.classPlantas import Planta
from Arduino.codigo_arduino import *
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

        # Mostrar información sobre la planta
        self.ui.label_3.setText(self.planta.nombre)

        # Para la actualización en tiempo real
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.actualizar_datos)
        self.timer.start(2000)  # Actualiza cada 2 segundos

    def actualizar_datos(self):
        sensor_data = read_sensors()
        if sensor_data:
            soil_humidity = sensor_data['SOIL']
            humidity_percentage = 100 - (soil_humidity / 10)

            humidity_percentage = max(0, min(100, humidity_percentage))  # valor entre 0 y 100

            self.ui.label_2.setText(f"{humidity_percentage:.2f}%")

            luminosity = sensor_data.get('LIGHT', 0)  # Si no está presente, toma 0 como valor predeterminado
            self.ui.label_4.setText(f"{luminosity} lux")

            # Estado de la bomba (lo que Arduino envía)
            pump_status = sensor_data.get('STATUS', 'Desconocido')
            self.ui.label_5.setText(f"{pump_status}")

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
