import sys
from PyQt5.QtWidgets import *

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

        self.savek = QPushButton("Save")

        ## Layout füllen
        layout.addRow("Vorname:", self.vorname)
        layout.addRow("Nachname:", self.nachname)
        layout.addRow("Geburtstag:", self.bday)
        layout.addRow("Adresse:", self.adr)
        layout.addRow("PLZ:", self.plz)
        layout.addRow("Ortschaft:", self.ort)
        layout.addRow("Land:", self.land)
        layout.addRow(self.savek)


        ## Menueleiste
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        self.save = QAction("Save", self)
        self.quit = QAction("Quit", self)
        filemenu.addAction(self.save)
        filemenu.addAction(self.quit)

        ## Fenster anzeigen
        self.show()


    def createConnect(self):
        self.quit.triggered.connect(self.close)
        self.save.triggered.connect(self.speicher)
        self.savek.clicked.connect(self.speicher)


    def close(self):
        self.close()

    def speicher(self):
        export = f"{self.vorname.text()},{self.nachname.text()},{self.bday.text()},{self.adr.text()},{self.plz.text()},{self.ort.text()},{self.land.currentText()}"

        f = open("output.txt", "w")
        f.write(export)
        f.close()

def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()       
    mainwindow.raise_()           
    app.exec_()                   

if __name__ == '__main__':
    main()