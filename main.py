import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from src.menu import MainWindow

"""
from Archivo convertido con pyside2-uic archivo.ui > interfaz.py
import nombre de la clase del archivo convertido
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
