import sys
import time
import logging
from datetime import datetime,timedelta

#from logging from 
from PyQt5 import QtCore,QtGui,QtWidgets
from NoteItemDrowUI import *
from  bd.db import *

#Класс который хранит всю информацию о заметках 
class NoteItemsUI():
    def __init__(self,ui):
        self.ui=ui
        self.ItemsData=dict()
        self.ItemsDrow=dict()
        self.spacerItem=QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

    def addItem(self,data):
        self.ItemsData[data.index]=data
        self.ItemsDrow[data.index]=NoteItemDrowUI(self.ui,data)

    def Drow(self,name):
        for index in self.ItemsData.keys():
            data=self.ItemsData[index]
            if( name=='Все заметки'):
                self.ItemsDrow[data.index].makeVisible()
            elif(data.name==name):
                self.ItemsDrow[data.index].makeVisible()
            else:
                self.ItemsDrow[data.index].makeHidden()
        self.ui.verticalLayout_10.removeItem(self.spacerItem)
        
        self.ui.verticalLayout_10.addItem(self.spacerItem)

    def deleteItem(self,data):
        
        self.ItemsDrow[data.index].makeHidden()
        self.ItemsDrow.pop(data.index,333)
        self.ItemsData.pop(data.index,333)
        self.Drow('Все заметки')
        deleteItemFromDB(data)


