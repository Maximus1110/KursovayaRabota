import sys
import time
import logging
from datetime import datetime,timedelta

#from logging from 
from PyQt5 import QtCore,QtGui,QtWidgets

from Forms.helpForm import *
from  Classes.bd.db import *




#Основной клас окна 
class MWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        self.parent=parent
        QtWidgets.QWidget.__init__(self, None)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        #Присвоение действия кнопке слева(Добавление фильтра пользователя)
        
        self.ui.pushButton.clicked.connect(self.clk)
    def clk(self):
        self.close()
        self.parent.setHidden(False)

         

        
   