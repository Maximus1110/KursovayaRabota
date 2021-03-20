
import sys
import time
import logging
from datetime import datetime,timedelta

#from logging from 
from PyQt5 import QtCore,QtGui,QtWidgets



#Управление календарём
class Calendar():
    def __init__(self,ui):
        self.ui=ui
        self.date=datetime.now()
        self.scrollAreas=[self.ui.scrollAreaWidgetContents_3,self.ui.scrollAreaWidgetContents_4,
            self.ui.scrollAreaWidgetContents_5,self.ui.scrollAreaWidgetContents_6]

        self.verticalLayouts=[self.ui.verticalLayout_11,self.ui.verticalLayout_16,
            self.ui.verticalLayout_17,self.ui.verticalLayout_18]

        self.textEdits=[self.ui.textEdit_4,self.ui.textEdit_5,self.ui.textEdit_6,self.ui.textEdit_7]  


        self.ui.pushButton_7.clicked.connect(self.clkRight)
        self.ui.pushButton_8.clicked.connect(self.clkLeft)
        
        for item in self.textEdits:
            item.setStyleSheet('color: black;')
            item.setStyleSheet('font: 75 12pt "MS Shell Dlg 2";background-color: rgb(146, 189, 108);')
        self.DrowAll()
           
    def oneText(self,text,scrollArea,verticalLayout,color="background-color: rgb(146, 189, 108);"):
        
        textEdit = QtWidgets.QTextEdit(scrollArea)
        textEdit.setEnabled(False)
        textEdit.setMinimumSize(QtCore.QSize(0, 50))
        textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        textEdit.setStyleSheet(color)
        textEdit.setObjectName("textEdit")
        textEdit.setText(text)
        verticalLayout.addWidget(textEdit)

    def returnDay(self,d):
        if(d==0):
            return('Пн')   
        elif(d==1):
            return('Вт')
        elif(d==2):
            return('Ср')   
        elif(d==3):
            return('Чт')
        elif(d==4):
            return('Пн')   
        elif(d==5):
            return('Сб')
        elif(d==6):
            return('Вс')  
    
    def returnMonth(self,m):
        if(m=='01'):
            return('янв')   
        elif(m=='02'):
            return('фев')
        elif(m=='03'):
            return('мар')   
        elif(m=='04'):
            return('апр')
        elif(m=='05'):
            return('май')   
        elif(m=='06'):
            return('июн')
        elif(m=='07'):
            return('июл')  
        elif(m=='08'):
            return('авг')
        elif(m=='09'):
            return('сен')   
        elif(m=='10'):
            return('окт')
        elif(m=='11'):
            return('ноя')   
        elif(m=='12'):
            return('дек')

    def Drow(self,day,scrollArea,verticalLayout,textEdit):

        
        T=[]
        dateNow=self.date+timedelta(days=day)
        textEdit.setPlainText(self.returnDay(dateNow.weekday())+' '+str(dateNow.date()))
        
        for index in self.ui.NoteItemsUI.ItemsData.keys():
            data=self.ui.NoteItemsUI.ItemsData[index]
            
            if(data.addToCalendar=='True'):
                if(data.everyWeek=='True'):
                    if(self.returnDay(dateNow.weekday())==data.data[:2]):
                        T.append(data)

                elif(data.everyWeek=='False'):
                    item=data.data.split(' ')
                    now=str(dateNow.date()).split('-')
                    if(item[1]==self.returnMonth(now[1]) and int(item[2])==int(now[2]) and item[3]==now[0]):
                        T.append(data)
        

        T=sorted(T, key=lambda d: d.startTime)   
        ltime='00:00'
        for d in T:
            if(ltime<d.startTime[:5]):
                text=f'{ltime}-{d.startTime[:5]}'
                self.oneText(text,scrollArea,verticalLayout)
            ltime=d.endTime[:5]
            IText=d.text
            if(len(IText)>15):
                IText=IText[:14]+"..."
            text=f'{d.startTime[:5]}-{d.endTime[:5]} \n{d.name} \n{IText}'
            self.oneText(text,scrollArea,verticalLayout,"background-color: rgb(235, 167, 33);")
        if(ltime!='24:00'):
            text=f'{ltime}-24:00'
            self.oneText(text,scrollArea,verticalLayout)

    def DrowAll(self):
        for i in range(4):
            self.Drow(i,self.scrollAreas[i],self.verticalLayouts[i],self.textEdits[i])    

    def Clear(self,verticalLayout):
        for i in reversed(range(verticalLayout.count())): 
            verticalLayout.itemAt(i).widget().setParent(None)

    def ClearAll(self):
        for i in range(4):
            self.Clear(self.verticalLayouts[i]) 

    def clkRight(self):
        self.ClearAll()
        self.date=self.date+timedelta(days=1)
        self.DrowAll()

    def clkLeft(self):
        self.ClearAll()
        self.date=self.date-timedelta(days=1)
        self.DrowAll()
