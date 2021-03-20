import sys
import time
import logging
from datetime import datetime,timedelta

#from logging from 
from PyQt5 import QtCore,QtGui,QtWidgets
from NoteItemData import *
from  bd.db import *

#Хранит информацию о графическом отбражении одной заметки
class NoteItemDrowUI():
    def __init__(self,ui,data):
        self.ui=ui
        self.data=data
        self.firstDrow()
    
    def firstDrow(self):

       
        self.groupBox = QtWidgets.QGroupBox(self.ui.scrollAreaWidgetContents_2)
        self.groupBox.setEnabled(True)

        self.groupBox.setMinimumSize(QtCore.QSize(100, 130))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 130))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)


        self.groupBox.setObjectName("groupBox"+self.data.index)
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout"+self.data.index)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)

        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plainTextEdit.setReadOnly(False)
        self.plainTextEdit.setObjectName("plainTextEdit"+self.data.index)

        
        insert=f'{self.data.data[:3]} {self.data.startTime[:5]}-{self.data.endTime[:5]} {self.data.data[3:]} \n\n\n'
        self.plainTextEdit.setPlainText(insert+self.data.text)

        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 4, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_0.setObjectName("pushButton_0"+self.data.index)
        self.gridLayout.addWidget(self.pushButton_0, 1, 1, 1, 1)

        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_1.setObjectName("pushButton_1"+self.data.index)
        self.gridLayout.addWidget(self.pushButton_1, 3, 1, 1, 1)
        self.ui.verticalLayout_10.addWidget(self.groupBox)
        

        self.groupBox.setTitle(self.data.name)
        self.pushButton_0.setText("Редактировать")
        self.pushButton_1.setText('Удалить')
        self.groupBox.setHidden(True)


        self.pushButton_1.clicked.connect(self.clkDelete)
        self.pushButton_0.clicked.connect(self.clkEdit)

    def makeVisible(self):
        self.groupBox.setVisible(True)

    def makeHidden(self):
        self.groupBox.setHidden(True)

    def clkDelete(self):
        self.ui.NoteItemsUI.deleteItem(self.data)

    def clkB0(self):
        d=self.data
        Item=NoteItemData(d.name,self.plainTextEdit.toPlainText(),d.data,d.startTime,d.endTime,d.everyWeek,d.addToCalendar)
        self.ui.NoteItemsUI.addItem(Item)
        addItemToDB(Item)
        self.ui.NoteItemsUI.deleteItem(self.data)        

    def clkB1(self):
        self.pushButton_0.setText("Редактировать")
        self.pushButton_1.setText('Удалить')
        self.plainTextEdit.setEnabled(False)
        insert=f'{self.data.data[:3]} {self.data.startTime[:5]}-{self.data.endTime[:5]} {self.data.data[3:]} \n\n\n'
        self.plainTextEdit.setPlainText(insert+self.data.text)

        self.pushButton_1.clicked.disconnect(self.clkB1)   
        self.pushButton_1.clicked.connect(self.clkDelete)
        self.pushButton_0.clicked.disconnect(self.clkB0) 
        self.pushButton_0.clicked.connect(self.clkEdit)

    def clkEdit(self):
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setPlainText('')
        self.pushButton_0.setText("Изменить")
        self.pushButton_1.setText('Отменить')
        

        self.pushButton_1.clicked.disconnect(self.clkDelete)   
        self.pushButton_1.clicked.connect(self.clkB1)

        self.pushButton_0.clicked.disconnect(self.clkEdit) 
        self.pushButton_0.clicked.connect(self.clkB0)