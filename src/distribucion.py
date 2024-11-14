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

        # Asegúrate de que el nombre del archivo JSON sea correcto
        self.rows, self.columns = self.leer_json('Datos/grilla.json')

        # Asegúrate de que el layout se llame "gridLayout" en tu archivo .ui
        self.crear_botones()

    def leer_json(self, archivo_json):
        """Lee un archivo JSON y devuelve las filas y columnas."""
        try:
            with open(archivo_json, 'r') as file:
                data = json.load(file)
            rows = data.get("rows", 1)        # Si no existe 'rows', usa 1 por defecto
            columns = data.get("columns", 1)  # Si no existe 'columns', usa 1 por defecto
            return rows, columns
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {archivo_json}")
            return 1, 1  # Valores predeterminados si falla la lectura del archivo

    def crear_botones(self):
        """Crea botones dinámicamente según las filas y columnas."""
        grid_layout = self.ui.gridLayout_2  # Verifica el nombre del layout en tu .ui
        
        for fila in range(self.rows):
            for columna in range(self.columns):
                boton = QPushButton(f"Botón {fila + 1}, {columna + 1}")
                grid_layout.addWidget(boton, fila, columna)
        # Establecer la hoja de estilo para el botón
                boton.setStyleSheet("""
                QPushButton {
                    background-color: #87b482;          /* Color de fondo verde */
                    border: 5px solid #59ad4b;          /* Borde de 2px y color verde más oscuro */
                    border-radius: 10px;                /* Bordes redondeados */
                    font: italic 30px;                  /* Letra en cursiva y tamaño 30px */
                    padding: 0px;                       /* Espaciado interno para ajustar el tamaño */
                }
                QPushButton:pressed {
                background-color: rgba(135, 180, 130, 120); /* Color al presionar (más translúcido) */
                }
                """)
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