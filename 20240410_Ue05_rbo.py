import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import urllib.parse

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()
        self.createConnect()

    def createLayout(self):
        ## Fenstertitel / Layout
        self.setWindowTitle("GUI Programmierung")
        layout = QFormLayout()
        self.setMinimumSize(800,200)

        ## Zentrierung der Widgets
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
        
        ## Widgets erstellen
        self.vorname = QLineEdit()
        self.nachname = QLineEdit()
        self.bday = QDateEdit()
        self.bday.setDisplayFormat("dd/MM/yyyy")
        self.adr = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()
        self.land = QComboBox()
        self.land.addItems(["Schweiz", "Deutschland", "Österreich", "andere"])

        self.showMapk = QPushButton("Auf Karte Anzeigen")
        self.loadk = QPushButton("Laden")
        self.savek = QPushButton("Save")

        ## Layout füllen
        layout.addRow("Vorname:", self.vorname)
        layout.addRow("Nachname:", self.nachname)
        layout.addRow("Geburtstag:", self.bday)
        layout.addRow("Adresse:", self.adr)
        layout.addRow("PLZ:", self.plz)
        layout.addRow("Ortschaft:", self.ort)
        layout.addRow("Land:", self.land)
        
        layout.addRow(self.showMapk)
        layout.addRow(self.loadk)
        layout.addRow(self.savek)

        ## Menueleiste
        menubar = self.menuBar()


        filemenu = menubar.addMenu("File")

        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)

        filemenu.addAction(self.save)
        filemenu.addAction(self.quit)


        viewmenu = menubar.addMenu("View")

        self.load = QAction("Datei Laden", self)
        self.showMap = QAction("Auf Karte anzeigen", self)

        viewmenu.addAction(self.load)
        viewmenu.addAction(self.showMap)

        ## Fenster anzeigen
        self.show()


    def createConnect(self):
        self.quit.triggered.connect(self.close)
        self.save.triggered.connect(self.speicher)
        self.load.triggered.connect(self.laden)
        self.showMap.triggered.connect(self.kartenansicht)
        self.savek.clicked.connect(self.speicher)
        self.loadk.clicked.connect(self.laden)
        self.showMapk.clicked.connect(self.kartenansicht)

    def close(self):
        self.close()

    def speicher(self):
       
        export = f"{self.vorname.text()},{self.nachname.text()},{self.bday.text()},{self.adr.text()},{self.plz.text()},{self.ort.text()},{self.land.currentText()}"

        filename, typ = QFileDialog.getSaveFileName(self,"Datensatz speichern", " ", "Text-File (*.txt)")

        f = open(filename, "w")
        f.write(export)
        f.close()

    def laden(self):
        filename, typ = QFileDialog.getOpenFileName(self,"Datensatz öffnen", " ", "Text-File (*.txt)")
        
        f = open(filename, "r")
        inhalt = f.read().split(",")
        if len(inhalt) == 7:
            self.vorname.setText(inhalt[0])
            self.nachname.setText(inhalt[1])

            self.bday.setDate(QDate.fromString(inhalt[2], "dd/MM/yyyy"))

            self.adr.setText(inhalt[3])
            self.plz.setText(inhalt[4])
            self.ort.setText(inhalt[5])

            index = self.land.findText(inhalt[6], Qt.MatchFixedString)
            if index >= 0:
                self.land.setCurrentIndex(index)

        else:
            QMessageBox.critical(self,"Datenformat Ungültig","Die angegebene Datei entsprciht nicht dem verlangten Datenformat")


    def kartenansicht(self):
        adrMap = f"{self.adr.text()}+{self.plz.text()}+{self.ort.text()}+{self.land.currentText()}"
        query = urllib.parse.quote(adrMap)
        link = f"https://www.google.ch/maps/place/{query}"
        QDesktopServices.openUrl(QUrl(link))

def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()