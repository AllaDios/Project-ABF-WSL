import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import json  # Importar el módulo para manejar JSON

from interfaces.ui_gestionar import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Gestión de Plantas")  # Establece el título de la ventana
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint)  # Deshabilita el botón de maximizar

        # Cargar los datos desde el archivo JSON
        self.plantas_data = self.cargar_datos_json('Datos/plantas.json')
        
        # Acceder al QScrollArea y su layout
        self.scroll_area = self.ui.scrollArea  # Asegúrate de que el nombre de tu QScrollArea sea 'scrollArea' en el archivo .ui
        content_widget = self.scroll_area.widget()
        
        # Asegurarte de que el widget tiene un layout
        if content_widget.layout() is None:
            # Si no tiene un layout, creamos uno
            layout = QVBoxLayout(content_widget)
        else:
            layout = content_widget.layout()
        
        # Crear botones con los nombres de las plantas
        self.botones = self.crear_botones(layout)

        # Opciones del ComboBox
        self.ui.comboBox.addItems(["+ Humedad", "- Humedad"])
        self.ui.comboBox.setInsertPolicy(QComboBox.InsertAlphabetically)

        # Conectar el botón para ordenar los botones
        self.ui.pushButton_8.clicked.connect(self.ordenar_botones)
        
    

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

    def crear_botones(self, layout):
        """
        Crear botones dentro del QScrollArea con los nombres de las plantas y asociarles un valor 'humedad'.
        """
        botones = []
        for planta in self.plantas_data:
            boton = QPushButton(planta['planta'])  # Crea el botón con el nombre de la planta
            boton.setFixedHeight(50)  # Establecer la altura fija del botón a 50px

            # Asignar la variable humedad al botón
            boton.humedad = planta['humedad']  # Asegúrate de que 'humedad' esté en los datos de planta

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

            layout.addWidget(boton)  # Añadir el botón al layout del QScrollArea
            botones.append(boton)  # Guardar el botón en la lista
        return botones

    def ordenar_botones(self):
        
        """
        Ordenar los botones dependiendo de la opción seleccionada en el ComboBox.
        """
        
        seleccion = self.ui.comboBox.currentText()

        # Guardar los datos esenciales (nombre y humedad) de los botones antes de eliminarlos
        datos_botones = [(boton.text(), boton.humedad) for boton in self.botones]

        # Ordenar los botones en función de la humedad
        if seleccion == "+ Humedad":
            datos_botones.sort(key=lambda x: x[1], reverse=True)  # Orden descendente por humedad
        else:
            datos_botones.sort(key=lambda x: x[1])  # Orden ascendente por humedad

        # Limpiar el layout antes de agregar los botones ordenados
        layout = self.scroll_area.widget().layout()

        # Eliminar los botones antiguos del layout
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()  # Eliminar el widget del layout

        # Crear y agregar nuevos botones ordenados al layout usando los datos almacenados
        self.botones = []  # Limpiar la lista de botones
        for nombre, humedad in datos_botones:
            nuevo_boton = QPushButton(nombre)  # Crear un nuevo botón con el nombre de la planta
            nuevo_boton.setFixedHeight(50)  # Mantener el tamaño de los botones
            nuevo_boton.humedad = humedad  # Mantener el valor de humedad

            # Establecer la hoja de estilo para el nuevo botón
            nuevo_boton.setStyleSheet("""
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

            # Agregar el nuevo botón al layout
            layout.addWidget(nuevo_boton)
            self.botones.append(nuevo_boton)  # Añadir el nuevo botón a la lista