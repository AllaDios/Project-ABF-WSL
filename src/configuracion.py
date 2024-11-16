import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics
from PyQt5 import QtCore
import json

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

    def abrir_ventana_MENU(self):
        from .menu import MenuWindow
        pos_x = self.geometry().x()
        pos_y = self.geometry().y()
        self.ventana_Menu = MenuWindow()
        self.ventana_Menu.move(pos_x, pos_y)
        self.ventana_Menu.show()
        self.close()