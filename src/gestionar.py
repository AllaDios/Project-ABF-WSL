import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import json
from classes.classPlantas import Planta

from interfaces.ui_gestionar import Ui_MainWindow


class GestionWindow(QMainWindow):
    def __init__(self, vivero):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Gestión de Plantas")  # Establece el título de la ventana
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint)  # Deshabilita el botón de maximizar

        # Guardar el objeto vivero
        self.vivero = vivero

        # Crear los botones con las plantas del vivero
        self.crear_botones()

        # Botón de Actualizar
        self.ui.pushButton_8.clicked.connect(self.ordenar_botones)

        # Botón para agregar las plantas
        self.ui.pushButton.clicked.connect(self.crear_planta_desde_comboBox2)

        # Botón para eliminar las plantas
        self.ui.pushButton_2.clicked.connect(self.eliminar_planta_desde_comboBox3)
        

        # Opciones del ComboBox
        self.ui.comboBox.addItems(["+ Humedad", "- Humedad"])
        self.ui.comboBox.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.ui.comboBox_2.setEditable(True)
        self.ui.comboBox_2.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.ui.comboBox_3.setEditable(True)
        self.ui.comboBox_3.setInsertPolicy(QComboBox.InsertAlphabetically)

    def crear_botones(self):
        """
        Crear botones dentro del QScrollArea con los nombres de las plantas del vivero.
        """
        # configuramos scroll area
        scroll_area = self.ui.scrollArea
        content_widget = scroll_area.widget()

        # Verificar y crear el layout si no existe
        layout = content_widget.layout()
        if layout is None:
            layout = QVBoxLayout(content_widget)
            content_widget.setLayout(layout)

        # Limpiar el layout antes de crear los botones
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # agregar botones al layout
        for planta in self.vivero.get_plantas():
            boton = QPushButton(planta.nombre)  
            boton.setFixedHeight(50)  # Ajustar el tamaño del botón
            boton.setStyleSheet("""  /* Estilo de los botones */
                QPushButton {
                    background-color: #87b482;  /* Color de fondo */
                    border: 5px solid #59ad4b;  /* Color del borde */
                    border-radius: 10px;        /* Bordes redondeados */
                    font: 24px Arial;           /* Tamaño y fuente */
                }
                QPushButton:pressed {
                    background-color: rgba(135, 180, 130, 120); /* Cambiar color al presionar */
                }
            """)
            layout.addWidget(boton)

    def ordenar_botones(self):
        """
        Ordenar los botones según la humedad seleccionada en el comboBox.
        """
        # Saber que opcion tiene el combo box
        opcion = self.ui.comboBox.currentText()

        # Ordenar las plantas por humedad de menor a mayor o de mayor a menor
        if opcion == "- Humedad":
            plantas_ordenadas = sorted(self.vivero.get_plantas(), key=lambda planta: planta.humedad, reverse=False)
        elif opcion == "+ Humedad":
            plantas_ordenadas = sorted(self.vivero.get_plantas(), key=lambda planta: planta.humedad, reverse=True)

        # Acceder al QScrollArea y su layout
        scroll_area = self.ui.scrollArea
        content_widget = scroll_area.widget()
        layout = content_widget.layout()

        # Limpiar los botones existentes en el layout
        if layout is not None:
            # Eliminar todos los widgets (botones) del layout
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget is not None:
                    widget.deleteLater()  # Elimina el widget de la memoria

        # Volver a agregar los botones ordenados al layout
        for planta in plantas_ordenadas:
            boton = QPushButton(planta.nombre)  # Crear botón con el nombre de la planta
            boton.setFixedHeight(50)  # Ajustar el tamaño del botón
            boton.setStyleSheet("""  /* Estilo de los botones */
                QPushButton {
                    background-color: #87b482;  /* Color de fondo */
                    border: 5px solid #59ad4b;  /* Color del borde */
                    border-radius: 10px;        /* Bordes redondeados */
                    font: 24px Arial;           /* Tamaño y fuente */
                }
                QPushButton:pressed {
                    background-color: rgba(135, 180, 130, 120); /* Cambiar color al presionar */
                }
            """)
            layout.addWidget(boton)

    def guardar_en_json(self):
        """
        Guarda las plantas del vivero en el archivo plantas.json.
        """
        try:
            with open("Datos/plantas.json", "w") as file:
                plantas_data = [
                    {"nombre": planta.nombre, "humedad": planta.humedad}
                    for planta in self.vivero.get_plantas()
                ]
                json.dump(plantas_data, file, indent=4)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo guardar en JSON: {str(e)}")

    def crear_planta_desde_comboBox2(self):
        """
        Crear una planta a partir del texto ingresado en comboBox_2.
        """
        texto_ingresado = self.ui.comboBox_2.currentText().strip()  # Obtener y limpiar el texto del comboBox_2

        if texto_ingresado: 
            # se crea un objeto Planta con el texto como nombre y humedad 0
            nueva_planta = Planta(nombre=texto_ingresado, humedad=0)

            # se agrega la planta al vivero
            self.vivero.agregar_planta(nueva_planta)

            # creamos el boton nuevo
            self.crear_botones()

            # guardar los cambios en el archivo JSON
            self.guardar_en_json()

            # borra el texto en comboBox_2 después de agregar la planta
            self.ui.comboBox_2.setCurrentText("")
            QMessageBox.information(self, "Éxito", "La planta se agregó correctamente.")

        else:
            QMessageBox.warning(self, "Error", "Debe ingresar un nombre válido para la planta.")

    def eliminar_planta_desde_comboBox3(self):
        texto_ingresado = self.ui.comboBox_3.currentText().strip()

        if texto_ingresado:
            planta_a_eliminar = self.vivero.buscar_planta_por_nombre(texto_ingresado)
            if planta_a_eliminar:
                self.vivero.eliminar_planta(planta_a_eliminar)
                # Guardar los cambios en el archivo JSON
                self.guardar_en_json()
                self.crear_botones()
                self.ui.comboBox_3.setCurrentText("")
                QMessageBox.information(self, "Éxito", "La planta se eliminó correctamente.")

            else:
                QMessageBox.warning(self, "Error", f"No se encontró la planta '{texto_ingresado}'.")
        else:
            QMessageBox.warning(self, "Error", "Debe ingresar un nombre válido para eliminar.")
            
    def abrir_ventana_menu(self):
        from .menu import MenuWindow  # Importamos la ventana de gestión
        # Capturamos la posición de la ventana actual antes de cerrarla
        pos_x = self.geometry().x()
        pos_y = self.geometry().y()
        self.ventana_menu = MenuWindow()
        # Establecemos la misma posición para la nueva ventana
        self.ventana_menu.move(pos_x, pos_y)
        self.ventana_menu.show()
        self.close()  # Cerramos la ventana de menú
