import sys
import time
import logging
from datetime import datetime,timedelta

#from logging from 
from PyQt5 import QtCore,QtGui,QtWidgets

#Хранит данные об одной заметке(отправляется в бд)
class NoteItemData():
    def __init__(self,name,text,data,startTime,endTime,
    everyWeek=False,addToCalendar=False,index='',createTime=''):
        self.name=name
        if(createTime==''):
            self.createTime=time.time()
        else:
            self.createTime=createTime

        if(index==''):
            self.index=name+'_'+str(self.createTime)
        else:
            self.index=index

        self.text=text
        self.data=data
        self.startTime=startTime
        self.endTime=endTime
        self.everyWeek=everyWeek
        self.addToCalendar=addToCalendar
