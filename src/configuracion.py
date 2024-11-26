import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFontMetrics
from PyQt5 import QtCore
from Arduino.codigo_arduino import *  # Importa la función de lectura de datos del Arduino

from interfaces.ui_configuracion import Ui_MainWindow

class ConfigurationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Configuración de Plantas")
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint)

        # Opciones del ComboBox
        self.ui.comboBox.addItems(["ON", "OFF"])
        self.ui.comboBox.setInsertPolicy(QComboBox.InsertAlphabetically)

        # Temporizador para actualizar el estado del tanque
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_tanque)
        self.timer.start(2000)  # Actualiza cada 4 segundos

    def actualizar_tanque(self):
        sensor_data = read_sensors()  # Asegúrate de que esta función lee el valor del sensor de nivel de agua

        if sensor_data:
            water_level = int(sensor_data.get('WATER', 0))  # Asegúrate de que 'WATER' sea el valor que esperas

            # Actualiza el label_2 dependiendo del valor del sensor de nivel de agua
            if water_level > 200:
                self.ui.label_2.setText("Tanque con agua")
            else:
                self.ui.label_2.setText("Tanque vacío")

    def abrir_ventana_MENU(self):
        from .menu import MenuWindow
        pos_x = self.geometry().x()
        pos_y = self.geometry().y()
        self.ventana_Menu = MenuWindow()
        self.ventana_Menu.move(pos_x, pos_y)
        self.ventana_Menu.show()
        self.close()