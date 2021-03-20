import sys
import time
import logging
from datetime import datetime,timedelta

#from logging from 
from PyQt5 import QtCore,QtGui,QtWidgets
from Forms.WelForm import *
import main
import helpW
from  Classes.bd.db import *




#Основной клас окна 
class MWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        #Присвоение действия кнопке слева(Добавление фильтра пользователя)
        self.ui.pushButton.clicked.connect(self.clkHelp)
        self.ui.pushButton_2.clicked.connect(self.clkStart)
    def clkHelp(self):
        self.setHidden(True)
        self.H = helpW.MWidget(self)
        self.H.setWindowTitle('Tutor Assistant')
        self.H.setWindowIcon(QtGui.QIcon('static/Icon.ico'))
        self.H.show()
    def clkStart(self):
        self.close()
        self.W = main.MWidget()
        self.W.setWindowTitle('Tutor Assistant')
        self.W.setWindowIcon(QtGui.QIcon('static/Icon.ico'))
        self.W.show()
         

        
        

if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   w = MWidget()
   w.setWindowTitle('Tutor Assistant')
   w.setWindowIcon(QtGui.QIcon('static/Icon.ico'))
   w.show()
   sys.exit(app.exec_())