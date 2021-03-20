import sys
import time
import logging
from datetime import datetime,timedelta

#from logging from 
from PyQt5 import QtCore,QtGui,QtWidgets
from  bd.db import *

#Класс хранит данные об одной кнопке фильтра имени (Которые слева)
class NameButton():
    def __init__(self,ui,name):
        self.ui=ui
        self.name=name
        self.DrowButton()
    def DrowButton(self):

        self.Button=QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents)

        self.Button.setObjectName(self.name)
        self.Button.setStyleSheet("")
        self.Button.setMinimumSize(QtCore.QSize(20, 28))
        self.ui.verticalLayout_19.addWidget(self.Button)

        self.Button.setText(self.name)
        self.Button.show()
        self.Button.clicked.connect(self.clkNameButton)

    def clkNameButton(self):
        self.ui.NoteItemsUI.Drow(self.name)
    def clkDelete(self):
        self.makeHidden()
        self.ui.UsersButtonsScrollArea.pop(self.name,333)
        deleteButtonFromDB(self.name)
        for elem in self.ui.NoteItemsUI.ItemsData.keys():
            if(self.ui.NoteItemsUI.ItemsData[elem].name==self.name):
                print(1)
                data=self.ui.NoteItemsUI.ItemsData[elem]
                print(data.name)
                #self.ui.NoteItemsUI.ItemsDrow[elem].makeHidden()
                #data.name='Остальные'
                #print(data.name)

                #self.ui.NoteItemsUI.addItem(data)
                #addItemToDB(data)

    def changeToDel(self):
        self.Button.clicked.disconnect(self.clkNameButton)
        self.Button.clicked.connect(self.clkDelete)

    def changeToStandart(self):
        self.Button.clicked.disconnect(self.clkDelete)
        self.Button.clicked.connect(self.clkNameButton)



    def setRedColor(self):
        self.Button.setStyleSheet("background-color: red;")
    def makeHidden(self):
        self.Button.setVisible(False)
    def setStandartColor(self):
        self.Button.setStyleSheet("")
