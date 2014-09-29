# Python 3.4.2rc1, PyQT5, PyPDF2

__author__ = "Johnny Xu"
__email__ = "xu.johnny92@gmail.com"

from PyPDF2 import PdfFileWriter, PdfFileReader
from PyQt5.QtCore import (Qt, QDir)
from PyQt5.QtWidgets import(QGridLayout, QLabel, QLineEdit, QTextEdit, QWidget,
    QPushButton, QFileDialog, QMessageBox)

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # Initiating UI Items
        self.pagesLabel = QLabel("Pages:")
        self.pageFirst = QLineEdit()
        self.pageFirst.setPlaceholderText("First Page #")
        self.pageLast = QLineEdit()
        self.pageLast.setPlaceholderText("Last Page #")
        self.execButton = QPushButton("&Execute")
        self.execButton.setToolTip("Execute the PDF split")

        self.iPathLabel = QLabel("Input File:")
        self.iPathText = QLineEdit()
        self.inputButton = QPushButton("&Load")
        self.inputButton.setToolTip("Load a PDF file")

        self.oPathLabel = QLabel("Output File:")
        self.oPathText = QLineEdit()
        self.outputButton = QPushButton("&Save")
        self.outputButton.setToolTip("Save as a PDF file")


        # Positioning GUI by grid format
        secLayout = QGridLayout()
        secLayout.addWidget(self.pageFirst, 0, 0)
        secLayout.addWidget(self.pageLast, 0, 1)

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.pagesLabel, 0, 0)
        mainLayout.addLayout(secLayout, 0, 1)
        mainLayout.addWidget(self.execButton, 0, 2)
        mainLayout.addWidget(self.iPathLabel, 1, 0)
        mainLayout.addWidget(self.iPathText, 1, 1)
        mainLayout.addWidget(self.inputButton, 1, 2)
        mainLayout.addWidget(self.oPathLabel, 2, 0)
        mainLayout.addWidget(self.oPathText, 2, 1)
        mainLayout.addWidget(self.outputButton, 2, 2)


        # Button Events
        self.inputButton.clicked.connect(self.loadFromFile)
        self.outputButton.clicked.connect(self.saveToFile)
        self.execButton.clicked.connect(self.runSplit)

        self.setLayout(mainLayout)
        self.setWindowTitle("PyDF Splitter")
        self.resize(600, 100)

    # Selects the input PDF to split
    def loadFromFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open PDF File", '', "PDF (*.pdf);;All Files (*)")
        self.iPathText.setText(fileName)

    # Sets the file where the output will be saved
    def saveToFile(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Save PDF File", '', "PDF (*.pdf);;All Files (*)")
        self.oPathText.setText(fileName)

    # Executes the PDF split on the input paramters
    def runSplit(self):
        pFirst = int(self.pageFirst.text()) - 1
        pLast = int(self.pageLast.text())
        iFile = self.iPathText.text()
        oFile = self.oPathText.text()

        # PDF Conversion
        output = PdfFileWriter()
        input1 = PdfFileReader(open(iFile, "rb"))

        for p in range(pFirst, pLast, 1):
            output.addPage(input1.getPage(p))

        outputStream = open(oFile, "wb")
        output.write(outputStream)
        outputStream.close()

if __name__ == '__main__':
    import sys

    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
