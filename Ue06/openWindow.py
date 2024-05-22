from PyQt5.QtWidgets import*
from PyQt5.uic import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import urllib.parse

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("2060_GP1/20_UEBUNGEN/06_Ue06/showmap.ui", self)

        self.mapshow.clicked.connect(self.funcmapshow)

    def funcmapshow(self):
        koordMap = f"{self.lon_edit.text()},{self.lat_edit.text()}"
        query = urllib.parse.quote(koordMap)
        link = f"https://www.google.ch/maps/place/{query}"
        QDesktopServices.openUrl(QUrl(link))


app = QApplication([])
window = Fenster()
window.show()
app.exec()