class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Gestion")  # Establece el título de la ventana
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint)  # Deshabilita el botón de maximizar
        self.ui.comboBox.addItems(["+ Humedad", "- Humedad"])
        self.ui.comboBox.setInsertPolicy(QComboBox.InsertAlphabetically)
        

        # Conectar el pushButton_8 al método ordenar_botones
        #self.ui.pushButton_8.clicked.connect(self.ordenar_botones)
        #La linea de arriba actualiza el combo box, es lo mismo que esta hecho en Qt disigner con los slots


        # Asignar valores de humedad a los botones
        self.ui.pushButton.setProperty("humedad", 30)
        self.ui.pushButton_2.setProperty("humedad", 50)
        self.ui.pushButton_3.setProperty("humedad", 10)
        self.ui.pushButton_4.setProperty("humedad", 80)
        self.ui.pushButton_5.setProperty("humedad", 60)
        #self.ui.pushButton_5.setText("")
        self.ui.pushButton_6.setProperty("humedad", 40)
    
        # Filtrar y agregar solo los botones con nombre al layout desde el principio
        self.agregar_botones_con_nombre()
        self.ordenar_botones()

    def agregar_botones_con_nombre(self):
        # Obtener los botones del layout
        botones = [
            self.ui.pushButton,
            self.ui.pushButton_2,
            self.ui.pushButton_3,
            self.ui.pushButton_4,
            self.ui.pushButton_5,
            self.ui.pushButton_6
        ]

        # Deshabilitar los botones que no tienen texto (vacíos)
        for boton in botones:
            if boton.text() == "":  # Si el botón no tiene texto
                boton.setEnabled(False)  # Deshabilitarlo (no será clickeable)
            else:
                boton.setEnabled(True)  # Asegurarse de que los botones con texto estén habilitados

        # Limpiar el layout existente
        while self.ui.verticalLayout_2.count():
            item = self.ui.verticalLayout_2.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        # Agregar los botones al layout (incluso los deshabilitados)
        for boton in botones:
            self.ui.verticalLayout_2.addWidget(boton)

    def ordenar_botones(self):
        # Obtener la selección del comboBox
        seleccion = self.ui.comboBox.currentText()

        # Obtener los botones del layout
        botones = [
            self.ui.pushButton,
            self.ui.pushButton_2,
            self.ui.pushButton_3,
            self.ui.pushButton_4,
            self.ui.pushButton_5,
            self.ui.pushButton_6
        ]

        # Separar los botones habilitados (con texto) y deshabilitados (sin texto)
        botones_con_texto = [btn for btn in botones if btn.text() != ""]
        botones_sin_texto = [btn for btn in botones if btn.text() == ""]

        # Ordenar los botones habilitados según su valor de "humedad"
        if seleccion == "+ Humedad":
            botones_con_texto.sort(key=lambda btn: btn.property("humedad"), reverse=True)
        elif seleccion == "- Humedad":
            botones_con_texto.sort(key=lambda btn: btn.property("humedad"))

        # Limpiar el layout existente
        while self.ui.verticalLayout_2.count():
            item = self.ui.verticalLayout_2.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        # Agregar los botones habilitados primero
        for boton in botones_con_texto:
            self.ui.verticalLayout_2.addWidget(boton)

        # Agregar los botones deshabilitados al final
        for boton in botones_sin_texto:
            self.ui.verticalLayout_2.addWidget(boton)