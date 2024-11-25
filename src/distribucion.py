import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics
from PyQt5 import QtCore
from classes.classPlantas import Planta  # importamos la clase Planta
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
        botones para cada planta en el vivero.
        Los botones serán cuadrados y mostrarán el nombre de cada planta.
        5 botones por fila.
        """
        # distribucion de botones
        grid_layout = self.ui.gridLayout_2

        # Limpiar el layout antes de agregar los botones
        for i in range(grid_layout.count()):
            widget = grid_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # obtenemos las plantas del vivero con el metodo de get_plantas
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
            # Conectar el botón a la función que abre InfoWindow
            boton.clicked.connect(lambda checked, p=planta: self.abrir_ventana_info(p))

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

    def abrir_ventana_info(self, planta, checked=None):
        from .info import InfoWindow
        pos_x = self.geometry().x()
        pos_y = self.geometry().y()
        # Crear una instancia de InfoWindow pasando la planta seleccionada
        self.ventana_info = InfoWindow(planta, self.vivero)
        self.ventana_info.move(pos_x, pos_y)
        self.ventana_info.show()
        self.close()  # Cerramos la ventana de menú
