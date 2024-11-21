import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
import json

from interfaces.ui_menu import Ui_MainWindow
from classes.classPlantas import Planta
from classes.classVivero import Vivero
from .humedad import obtener_humedad
from .temperatura import obtener_temperatura

class MenuWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Menu de Plantas")  # Establece el título de la ventana
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint)  # Deshabilita el botón de maximizar
        
        # Conectamos el botón con la función que abre la ventana de gestión
        self.pushButton_3.clicked.connect(self.abrir_ventana_gestion)

        # conectamos el botón con la función que abre la ventana de distribucion
        self.pushButton_2.clicked.connect(self.abrir_ventana_distribucion)

        # Conectamos el botón con la función que abre la ventana de configuracion
        self.pushButton.clicked.connect(self.abrir_ventana_configuracion)

        # Humedad
        humedad = obtener_humedad()
        self.label_4.setText(humedad)

        # Temperatura
        temperatura = obtener_temperatura()
        self.label_5.setText(temperatura)  

        # Cargar los datos desde el archivo JSON
        self.plantas_data = self.cargar_datos_json('Datos/plantas.json')
        
        # recorrer plantas data y por cada elementos crear una planta
        plantas = []
        for i in self.plantas_data : 
            planta = Planta(i['nombre'], i['humedad'])
            plantas.append(planta)
        
        #Creo el vivero
        self.vivero = Vivero('Mi Vivero', plantas)
        print (self.vivero.nombre)

    def cargar_datos_json(self, archivo):
        """
        Cargar los datos desde un archivo JSON.
        """
        try:
            with open(archivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: El archivo {archivo} no se encuentra.")
            return []
        except json.JSONDecodeError:
            print(f"Error: El archivo {archivo} no tiene formato JSON válido.")
            return []

    def abrir_ventana_gestion(self):
        from .gestionar import GestionWindow  # Importamos la ventana de gestión#+
        # Capturamos la posición de la ventana actual antes de cerrarla
        pos_x = self.geometry().x()
        pos_y = self.geometry().y()
        self.ventana_gestion = GestionWindow(self.vivero)
        # Establecemos la misma posición para la nueva ventana
        self.ventana_gestion.move(pos_x, pos_y)
        self.ventana_gestion.show()
        self.close()  # Cerramos la ventana de menú

    def abrir_ventana_distribucion(self):
        from .distribucion import DistributionWindow  # Importamos la ventana de gestión#+
        # Capturamos la posición de la ventana actual antes de cerrarla
        pos_x = self.geometry().x()
        pos_y = self.geometry().y()
        self.ventana_distribucion = DistributionWindow(self.vivero)
        # Establecemos la misma posición para la nueva ventana
        self.ventana_distribucion.move(pos_x, pos_y)
        self.ventana_distribucion.show()
        self.close()  # Cerramos la ventana de menú

    def abrir_ventana_configuracion(self):
        from .configuracion import ConfigurationWindow  # Importamos la ventana de gestión#+
        # Capturamos la posición de la ventana actual antes de cerrarla
        pos_x = self.geometry().x()
        pos_y = self.geometry().y()
        self.ventana_configuracion = ConfigurationWindow()
        # Establecemos la misma posición para la nueva ventana
        self.ventana_configuracion.move(pos_x, pos_y)
        self.ventana_configuracion.show()
        self.close()  # Cerramos la ventana de menú

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())