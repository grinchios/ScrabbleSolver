# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import App

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Scrabble Solver")
        MainWindow.resize(400, 362)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 181, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 181, 17))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 30, 51, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.run)
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 10, 104, 16))
        self.lineEdit.setObjectName("textEdit")
        self.lineEdit.returnPressed.connect(self.pushButton.click)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 40, 104, 16))
        self.lineEdit_2.setObjectName("textEdit_2")
        self.lineEdit_2.returnPressed.connect(self.pushButton.click)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 70, 104, 16))
        self.lineEdit_3.setObjectName("textEdit_3")
        self.lineEdit_3.returnPressed.connect(self.pushButton.click)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 100, 381, 192))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter your letters"))
        self.label_2.setText(_translate("MainWindow", "Specify start letters"))
        self.label_3.setText(_translate("MainWindow", "Specify ending letters"))
        self.pushButton.setText(_translate("MainWindow", "GO!"))
    
    def closeEvent(self, event):  #asks the user if they're sure they wanna end the program
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
    def run(self):  #checks before running
        flag = False
        if str(self.lineEdit.text()) != '':  #checks if anything was entered
            check = str(self.lineEdit.text())
            flag = True
        else:
            self.textBrowser.setText('')
            self.textBrowser.setText("You haven't entered any of your letters...")            
        if str(self.lineEdit_2.text()) == '':  #checks if start is filled
            check2 = '0'
        else:
            check2 = str(self.lineEdit_2.text())
            flag = True            
        if str(self.lineEdit_3.text()) == '':   #checks if end is filled
            check3 = '0'
        else:
            check3 = str(self.lineEdit_3.text())
            flag = True
        if flag == True:
            printWords = App.mainfunc.App(check, check2, check3)
            self.textBrowser.setText('')
            self.textBrowser.setText("Your possible words are:\n" + printWords)
        #outputs ^^
        return self 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

