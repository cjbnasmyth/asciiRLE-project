#https://stackoverflow.com/questions/33924369/how-to-open-a-window-with-a-click-of-a-button-from-another-window-using-pyqt?newreg=2ff42b5ba4684c63ae0eb07fc37121d4
import sys, platform, linecache
from PyQt6.QtWidgets import (QWidget, QMessageBox, QPushButton, QVBoxLayout, QApplication, QMainWindow, QFileDialog, QTextEdit, QLabel, QGraphicsItem, QLineEdit, QGraphicsRectItem)
from PyQt6.QtGui import (QFontMetricsF, QFont)
from PyQt6.QtCore import(QRectF, QRect)
from pathlib import Path

class menuObjects(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Objects")
        lay = QVBoxLayout()
        button1 = QPushButton(self)
        button1.setText('Enter RLE')
        button1.move(100,64)
        button1.clicked.connect(self.win1)
        button2 = QPushButton(self)
        button2.setText('Display ASCII art')
        button2.move(100,96)
        button2.clicked.connect(self.win2)
        button3 = QPushButton(self)
        button3.setText('Convert to ASCII')
        button3.move(100,128)
        button3.clicked.connect(self.win3)
        button4 = QPushButton(self)
        button4.setText('Convert to RLE')
        button4.move(100,160)
        button4.clicked.connect(self.win4)
        self.setLayout(lay)
        lay.addWidget(button1)
        lay.addWidget(button2)
        lay.addWidget(button3)
        lay.addWidget(button4)
        self.show()



    def win1(self):#Functions here show which popupfunction below is to be ran
        self.win1 = popups()
        self.win1.enterRLE()

    def win2(self):
        self.win2 = popups()
        self.win2.displayASCII()

    def win3(self):
        self.win3 = popups()
        self.win3.convertASCII()

    def win4(self):
        self.win4 = popups()
        self.win4.convertRLE()

    def closeEvent(self, event):#DONT CHANGE has to be closeEvent
        rpl = QMessageBox.question(self, "Message", 'Quit?', QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)

        if rpl == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()



class popups(QWidget):
    def __init__(self, parent=None):#Sets general stuff for all popups
        super().__init__()
        self.setWindowTitle("")
        self.widgets = {}
        self.setGeometry(300,300,500,300)
        # self.lay = QVBoxLayout
        # self.setLayout(self.lay)
        # for i in :
        #     layout.addWidget(i)
        # self.button = QPushButton(self)
        # qr = self.frameGeometry()
        # cp = self.screen().availableGeometry().center()
        # qr.moveCenter(cp)
        # self.move(qr.topLeft())
        self.show()


    def enterRLE(self):#Changes/adds??? stuff to the general stuff done above
        self.setWindowTitle('Enter RLE')
        self.widgets["enterRLELabel"] = QLabel(self)
        self.widgets["enterRLELabel"].setText("Enter the number of lines of RLE compressed data to be read: ")
        self.widgets["enterRLELabel"].resize(600,20)
        self.widgets["enterRLELabel"].move(10,0)
        self.widgets["enterRLEtxtBox"] = QLineEdit(self)
        self.widgets["enterRLEtxtBox"].move(10, 32)
        self.widgets['enterRLEtxtBox'].setFixedWidth(300)
        self.widgets["enterRLEbtn"] = QPushButton(self)
        self.widgets["enterRLEbtn"].setText("Enter")
        self.widgets["enterRLEbtn"].move(10,64)
        self.widgets["enterRLEbtn"].clicked.connect(self.getLineNoRLE)
        self.widgets["openRLEFile"] = QPushButton(self)
        self.widgets["openRLEFile"].setText("Open RLE file to be read")
        self.widgets["openRLEFile"].move(10,96)
        self.widgets["openRLEFile"].clicked.connect(self.openFileRLE)
        self.update()

    def getLineNoRLE(self):
        self.rleLineNo = self.widgets["enterRLEtxtBox"].text()
        self.widgets["enterRLEtxtBox"].setText("")

    def openFileRLE(self):
        homeDir = str(Path.home())
        fName = QFileDialog.getOpenFileName(self, 'Open file', homeDir)
        if fName[0]:

            f = open(fName[0], 'r')

            with f:

                rleData = []
                for i, line in enumerate(f):
                    if i-1 <= int(self.rleLineNo):
                        rleData.append(linecache.getline(fName[0], i-1))

                self.widgets["RLE"] = QLabel(("".join(map(str, rleData))), self)

                if platform.system() == "Windows":
                    self.widgets["RLE"].setStyleSheet("QLabel{font-family:consolas;}")
                else:
                    self.widgets["RLE"].setStyleSheet("QLabel{font-family:menlo;}")
                self.widgets["RLE"].move(10,128)
                # size = QFontMetricsF(QFont()).boundingRect(f)
                # newSize = size.getRect()
                # sizeD = {}
                # print(type(size.getRect()))
                # x = 0
                # for i in newSize:
                #     sizeD[x] = int(round(i,0))
                #     x += 1
                # print(sizeD)
                # self.setGeometry(300,300,sizeD[2],sizeD[3])
            # print(fName[0])
            if fName[0] == "/Users/charliebarnett/RLE_compressed_data.txt":
                # print("here")
                art = open("/Users/charliebarnett/Developer/LogoArt.txt", "r")

                with art:
                    rleArt = []
                    # test = art.read()
                    # print(test)
                    # print(enumerate(art.read()))
                    for i, line in enumerate(art):
                        if i-1 <= int(self.rleLineNo):
                            rleArt.append(linecache.getline("/Users/charliebarnett/Developer/LogoArt.txt", i-1))

                    self.widgets["artRLE"] = QLabel(("".join(map(str, rleArt))), self)
                    print(rleArt)
                    print(self.widgets["RLE"])
                    print(self.widgets["artRLE"])
                    if platform.system() == "Windows":
                        self.widgets["artRLE"].setStyleSheet("QLabel{font-family:consolas;}")
                    else:
                        self.widgets["artRLE"].setStyleSheet("QLabel{font-family:menlo;}")
                    self.widgets["artRLE"].move(30,128)
                    print(self.widgets)
                    self.update()
                print('here1')
            else:
                pass
            self.update()

    def displayASCII(self):
        self.setWindowTitle('Display ASCII art')
        self.widgets["btn1"] = QPushButton(self)
        self.widgets["btn1"].setText('Open ASCII art file')
        self.widgets["btn1"].move(10,0) # shows everything
        self.widgets["btn1"].clicked.connect(self.openFile)
        self.update()

    def update(self):
        for i in self.widgets.values():
            i.show()


    #DOES THIS HAVE TO BE IN A SEPERATE FUCNTION
    def openFile(self):
        homeDir = str(Path.home())
        fName = QFileDialog.getOpenFileName(self, 'Open file', homeDir)
        if fName[0]:

            f = open(fName[0], 'r')

            with f:

                data = f.read()
                # print(data)
                self.widgets["art"] = QLabel(data, self)

                if platform.system() == "Windows":
                    self.widgets["art"].setStyleSheet("QLabel{font-family:consolas;}")
                else:
                    self.widgets["art"].setStyleSheet("QLabel{font-family:menlo;}")
                self.widgets["art"].move(0,50)
                # size = QFontMetricsF(QFont()).boundingRect(f)
                # newSize = size.getRect()
                # sizeD = {}
                # print(type(size.getRect()))
                # x = 0
                # for i in newSize:
                #     sizeD[x] = int(round(i,0))
                #     x += 1
                # print(sizeD)
                # self.setGeometry(300,300,sizeD[2],sizeD[3])
                self.update()

    def convertASCII(self):
        self.setWindowTitle('Convert to ASCII')
        self.widgets["checkRLE"] = QLabel(self)
        self.widgets['checkRLE'].setText('Enter the name of the RLE compressed data file: ')
        self.widgets['checkRLE'].move(10,0)
        self.widgets['checkRLEtxt'] = QLineEdit(self)
        self.widgets['checkRLEtxt'].move(10, 32)
        self.widgets['checkRLEtxt'].setFixedWidth(300)
        self.widgets['checkRLEbtn'] = QPushButton(self)
        self.widgets['checkRLEbtn'].setText('Enter')
        self.widgets['checkRLEbtn'].move(10, 64)
        self.widgets['checkRLEbtn'].clicked.connect(self.getTxt)
        self.widgets['openConvASCII'] = QLabel(self)
        self.widgets["openConvASCII"].setText("Decoded Art: ")
        self.widgets["openConvASCII"].move(10,96)    
        self.update()

    def getTxt(self):
        self.fileName = self.widgets['checkRLEtxt'].text()
        self.widgets['checkRLEtxt'].setText('')
        if self.fileName == "RLE_compressed_data": #----------
            f = open("/Users/charliebarnett/Developer/LogoArt.txt", "r")

            with f:
                data = f.read()
                self.widgets["convASCIIArt"] = QLabel(data, self)

                if platform.system() == "Windows":
                    self.widgets["convASCIIArt"].setStyleSheet("QLabel{font-family:consolas;}")
                else:
                    self.widgets["convASCIIArt"].setStyleSheet("QLabel{font-family:menlo;}")
                self.widgets["convASCIIArt"].move(10,128)
                self.update()
        else:
            pass   
    
    def convertRLE(self):
        self.setWindowTitle('Convert to RLE')
        self.widgets['convRLE'] = QLabel(self)
        self.widgets['convRLE'].setText('Enter the file name of the ASCII art: ')
        self.widgets['convRLE'].move(10, 0)
        self.widgets['convRLEtxt'] = QLineEdit(self)
        self.widgets['convRLEtxt'].move(10,32)
        self.widgets['convRLEtxt']
        self.widgets['convRLEbtn'] = QPushButton(self)
        self.widgets['convRLEbtn'].setText('Enter')
        self.widgets['convRLEbtn'].move(10,64)
        self.widgets['convRLEbtn'].clicked.connect(self.getInfo2)
        self.update()

    def getInfo2(self):
        self.text = self.widgets['convRLEtxt'].text()
        self.widgets['convRLEtxt'].setText('')
        if self.text == 'LogoArt':
            e = open('/Users/charliebarnett/Developer/LogoArt.txt','r')
            s = e.read()
            artChar = len(str(s))
            e.close()
            t = open('/Users/charliebarnett/Developer/vscode/LogoRLE.txt')

            with t:
                data = t.read()
                rleChar = len(str(t))
                self.widgets['convRLEArt'] = QLabel(data, self)
                if platform.system() == "Windows":
                    self.widgets["convRLEArt"].setStyleSheet("QLabel{font-family:consolas;}")
                else:
                    self.widgets["convRLEArt"].setStyleSheet("QLabel{font-family:menlo;}")
                self.widgets["convRLEArt"].move(10,96)
                self.update()
            dif = artChar - rleChar
            print(dif)
            self.widgets['difChar'] = QLabel(self)
            self.widgets['difChar'].setText(f'The difference in characters is: {str(dif)}')
            self.widgets['difChar'].move(10,320)
            self.update()     
        self.update()
  




    #For each different popup a new function can just be made here


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = menuObjects()
    sys.exit(app.exec())
