import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import json  # Importar el módulo para manejar JSON

from interfaces.ui_gestionar import Ui_MainWindow

class GestionWindow(QMainWindow):
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

        self.ui.comboBox_2.addItems(["Opción 1", "Opción 2", "Opción 3"])
        self.ui.comboBox_2.setEditable(True)
        self.ui.comboBox_2.setInsertPolicy(QComboBox.InsertAlphabetically)
        
        self.ui.comboBox_3.addItems(["Opción 1", "Opción 2", "Opción 3"])
        self.ui.comboBox_3.setEditable(True)
        self.ui.comboBox_3.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.ui.pushButton.clicked.connect(self.agregar_en_json)
        self.ui.pushButton_2.clicked.connect(self.eliminar_en_json)

    def agregar_en_json(self):
        """Guarda el contenido del comboBox_2 en un archivo JSON."""
        texto = self.ui.comboBox_2.currentText()

        # Verificar que no esté vacío
        if not texto:
            QMessageBox.warning(self, "Advertencia", "El campo del comboBox está vacío. Por favor, ingresa un valor.")
            return

        # Cargar datos existentes de 'plantas.json'
        try:
            with open('Datos/plantas.json', 'r') as file:
                plantas = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            plantas = []

        # Añadir el nuevo dato al JSON
        nueva_planta = {
            "planta": texto,
            "humedad": 0  # Puedes cambiar este valor según tus necesidades
        }
        plantas.append(nueva_planta)

        # Guardar los datos actualizados en 'plantas.json'
        with open('Datos/plantas.json', 'w') as file:
            json.dump(plantas, file, indent=4)

        # Mostrar mensaje de confirmación
        QMessageBox.information(self, "Éxito", f"'{texto}' ha sido agregado a plantas.json")

    def eliminar_en_json(self):
        """Elimina el texto seleccionado en el comboBox_3 de plantas.json."""
        texto_a_eliminar = self.ui.comboBox_3.currentText()

        # Verificar que se haya seleccionado un texto
        if not texto_a_eliminar:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una planta para eliminar.")
            return

        # Cargar los datos desde plantas.json
        try:
            with open('Datos/plantas.json', 'r') as file:
                plantas = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            QMessageBox.warning(self, "Error", "No se pudo leer el archivo plantas.json.")
            return

        # Buscar si la planta está en el JSON y eliminarla
        planta_encontrada = False
        for planta in plantas:
            if planta['planta'] == texto_a_eliminar:
                plantas.remove(planta)  # Eliminar la planta del JSON
                planta_encontrada = True
                break

        if not planta_encontrada:
            QMessageBox.warning(self, "No encontrado", f"La planta '{texto_a_eliminar}' no se encuentra en el archivo.")
            return

        # Guardar los datos actualizados en plantas.json
        try:
            with open('Datos/plantas.json', 'w') as file:
                json.dump(plantas, file, indent=4)
            QMessageBox.information(self, "Éxito", f"'{texto_a_eliminar}' ha sido eliminado de plantas.json.")
        except IOError:
            QMessageBox.warning(self, "Error", "No se pudo guardar el archivo plantas.json.")
        
    def abrir_ventana_menu(self):
        from .menu import MenuWindow  # Importamos la ventana de gestión#+
        # Capturamos la posición de la ventana actual antes de cerrarla
        pos_x = self.geometry().x()
        pos_y = self.geometry().y()
        self.ventana_menu = MenuWindow()
        # Establecemos la misma posición para la nueva ventana
        self.ventana_menu.move(pos_x, pos_y)
        self.ventana_menu.show()
        self.close()  # Cerramos la ventana de menú
    
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