import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics
from PyQt5 import QtCore
from classes.classPlantas import Planta  # Asegúrate de importar la clase Planta
from interfaces.ui_distribucion import Ui_MainWindow

class DistributionWindow(QMainWindow):
    def __init__(self, vivero):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Distribución de Plantas")
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint)

        self.vivero = vivero 

        # Llamar a la función que creará los botones
        self.crear_botones()

    def crear_botones(self):
        """
        Crear botones en un QGridLayout para cada planta en el vivero.
        Los botones serán cuadrados y mostrarán el nombre de cada planta.
        Se agregarán 5 botones por fila.
        """
        # Obtener el layout de la interfaz (gridLayout_2 en este caso)
        grid_layout = self.ui.gridLayout_2  # Usar el gridLayout_2

        # Limpiar el layout antes de agregar los botones
        for i in range(grid_layout.count()):
            widget = grid_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Obtener las plantas del vivero
        plantas = self.vivero.get_plantas()

        # Definir cuántos botones caben por fila
        botones_por_fila = 5

        # Crear botones para cada planta
        for i, planta in enumerate(plantas):
            # Crear un botón para la planta
            boton = QPushButton(planta.nombre)
            boton.setStyleSheet("""
                QPushButton {
                    background-color: #87b482;
                    border: 5px solid #59ad4b;
                    border-radius: 10px;
                    font: 16px Arial;
                    text-align: center;
                }
                QPushButton:pressed {
                    background-color: rgba(135, 180, 130, 120);
                }
            """)

            # Añadir el botón al layout
            fila = i // botones_por_fila  # Calcular la fila (cada 5 botones pasa a una nueva fila)
            columna = i % botones_por_fila  # Calcular la columna en la fila actual

            grid_layout.addWidget(boton, fila, columna)

            # Asegurar que el botón se ajuste a su celda, manteniendo una proporción cuadrada
            boton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            grid_layout.setRowStretch(fila, 1)
            grid_layout.setColumnStretch(columna, 1)

    def abrir_ventana_Menu(self):
        from .menu import MenuWindow
        pos_x = self.geometry().x()
        pos_y = self.geometry().y()
        self.ventana_Menu = MenuWindow()
        self.ventana_Menu.move(pos_x, pos_y)
        self.ventana_Menu.show()
        self.close()
