import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics
from PyQt5 import QtCore
import json

from interfaces.ui_distribucion import Ui_MainWindow

class DistributionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Distribución de Plantas")
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint)
        
        # Leer filas y columnas del archivo grilla.json
        self.rows, self.columns = self.leer_json_grilla('Datos/grilla.json')

        # Leer nombres de plantas del archivo plantas.json
        self.plantas = self.leer_json_plantas('Datos/plantas.json')

        # Crear botones dinámicamente en la grilla
        self.crear_botones()

    def leer_json_grilla(self, archivo_json):
        """Lee un archivo JSON y devuelve las filas y columnas."""
        try:
            with open(archivo_json, 'r') as file:
                data = json.load(file)
            rows = data.get("rows", 1)
            columns = data.get("columns", 1)
            return rows, columns
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {archivo_json}")
            return 1, 1
        except json.JSONDecodeError:
            print(f"Error: No se pudo parsear el archivo {archivo_json}")
            return 1, 1

    def leer_json_plantas(self, archivo_json):
        """Lee un archivo JSON y devuelve una lista de nombres de plantas."""
        try:
            with open(archivo_json, 'r') as file:
                data = json.load(file)
            plantas = [item['planta'] for item in data]
            return plantas
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {archivo_json}")
            return []
        except json.JSONDecodeError:
            print(f"Error: No se pudo parsear el archivo {archivo_json}")
            return []

    def crear_botones(self):
        """Crea botones dinámicamente según las filas, columnas y plantas disponibles."""
        grid_layout = self.ui.gridLayout_2
        
        # Contador para llevar la cuenta de las plantas
        planta_index = 0

        for fila in range(self.rows):
            for columna in range(self.columns):
                boton = QPushButton()
                
                # Si hay una planta disponible, usamos su nombre
                if planta_index < len(self.plantas):
                    boton.setText(self.plantas[planta_index])
                    planta_index += 1
                else:
                    # Si no hay más plantas, dejar el botón vacío y deshabilitarlo
                    boton.setText("")
                    boton.setEnabled(False)

                # Ajustar el botón para ser cuadrado y redimensionable
                boton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                # Ajustar el tamaño del texto para que se ajuste al botón
                self.ajustar_fuente(boton)

                # Añadir el botón al grid layout
                grid_layout.addWidget(boton, fila, columna)

                # Establecer la hoja de estilo para el botón
                boton.setStyleSheet("""
                QPushButton {
                    background-color: #87b482;
                    border: 5px solid #59ad4b;
                    border-radius: 10px;
                    font: italic 16px;
                    padding: 0px;
                }
                QPushButton:pressed {
                    background-color: rgba(135, 180, 130, 120);
                }
                """)

    def ajustar_fuente(self, boton):
        """Ajusta la fuente del botón para que el texto se ajuste al tamaño del botón."""
        font = boton.font()
        font.setPointSize(16)  # Tamaño de fuente por defecto
        boton.setFont(font)

        # Obtener métricas de la fuente
        fm = QFontMetrics(font)
        text = boton.text()

        # Reducir el tamaño de la fuente si el texto no cabe en el botón
        while fm.width(text) > boton.width() - 10 and font.pointSize() > 8:
            font.setPointSize(font.pointSize() - 1)
            boton.setFont(font)
            fm = QFontMetrics(font)

    def abrir_ventana_Menu(self):
        from .menu import MenuWindow
        pos_x = self.geometry().x()
        pos_y = self.geometry().y()
        self.ventana_Menu = MenuWindow()
        self.ventana_Menu.move(pos_x, pos_y)
        self.ventana_Menu.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = DistributionWindow()
    ventana.show()
    sys.exit(app.exec_())