import sys
import time
import logging
from datetime import datetime,timedelta

#from logging from 
from PyQt5 import QtCore,QtGui,QtWidgets
from Forms.form import *
from  Classes.bd.db import *


class Widget(QtWidgets.QWidget, Ui_main):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setupUi(self)



# Класс который хранит всю информацию о заметках 
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
            elif(name=='Остальные'):
                b=list(self.ui.UsersButtonsScrollArea)
                if((self.ItemsData[index].name not in b) or (self.ItemsData[index].name=='Остальные')):
                    self.ItemsDrow[data.index].makeVisible()
                else:
                    self.ItemsDrow[data.index].makeHidden()
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


        
#Основной клас окна 
class MWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=Widget()
        self.ui.setupUi(self)
        #Присвоение действия кнопке слева(Добавление фильтра пользователя)
        self.ui.nameAddButton.clicked.connect(self.clkNameAddButton)

        #Редактируем некоторые визуальные поля и убираем тестувую заметку
        self.ui.lineEditName.setPlaceholderText("Введите имя пользователя")
        self.ui.enterText.setPlaceholderText('Место для вашей заметки')
        self.ui.groupBox_18.setHidden(True)

        #Работа с динамическим добавлением кнопок в ScrollArea
        #Cоздаём словарь кнопок
        self.ui.UsersButtonsScrollArea=dict()
        

        #Прикрепляем класс для хранения заметок
        self.ui.NoteItemsUI=NoteItemsUI(self.ui)
    
        #Прикрепляем действие для добавления новой записи
        self.ui.buttonAdd.clicked.connect(self.clkItemAddButton)

        
        self.ui.startTime.setTime(QtCore.QTime(16,30,0))
        self.ui.endTime.setTime(QtCore.QTime(18,0,0))
        self.ui.selectDate.setDate(QtCore.QDate.currentDate())
        #Дублируем данные о записях из БД при первом запуске
        for i in getItemDataFromDB():
            a=NoteItemData(i[1],i[2],i[4],i[5],i[6],i[7],i[8],i[0],i[3])
            self.ui.NoteItemsUI.addItem(a)
        

        #Очищаем Правый ComboBox
        self.ui.selectName.clear()

        #Дублируем данные о кнопках из БД при первом запуске
        for i in getButtonNameFromDB():
            self.ui.UsersButtonsScrollArea[i[0]]=NameButton(self.ui,i[0])
            #Добавляем возможные имена в ComboBox
            if(i[0]!='Все заметки'):
                self.ui.selectName.addItem(i[0])
        self.ui.NoteItemsUI.Drow('Все заметки')

        
        #ерунда для прижатия кнопок 
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ui.verticalLayout_19.addItem(self.spacerItem)

        #Убираем кнопки из дизайна
        #self.ui.pushButton_5.setVisible(False)
        self.ui.pushButton_5.setText('Удалить участника')
        self.ui.pushButton_5.clicked.connect(self.clkDelete)
        self.ui.pushButton_6.setVisible(False)

        self.ui.Calendar=Calendar(self.ui)
        self.setDefCalendar()

        
        self.ui.mainTab.tabBarClicked.connect(self.clkTab)
        self.ui.mainTab.setTabVisible(1,False)
        self.ui.mainTab.setTabVisible(1,True)
    def clkTab(self):
        self.ui.Calendar.ClearAll()
        self.ui.Calendar.DrowAll()

    def clkDelete(self):
        for k in self.ui.UsersButtonsScrollArea.keys():
            if(k!='Все заметки' and k!='Остальные'):
                self.ui.UsersButtonsScrollArea[k].changeToDel()
                self.ui.UsersButtonsScrollArea[k].setRedColor()
        self.ui.pushButton_5.setText('Отмена')
        self.ui.pushButton_5.clicked.disconnect(self.clkDelete)
        self.ui.pushButton_5.clicked.connect(self.clkBack)


    def clkBack(self):
        self.ui.pushButton_5.setText('Удалить участника')
        self.ui.pushButton_5.clicked.disconnect(self.clkBack)
        self.ui.pushButton_5.clicked.connect(self.clkDelete)
        for k in self.ui.UsersButtonsScrollArea.keys():
             if(k!='Все заметки' and k!='Остальные'):
                self.ui.UsersButtonsScrollArea[k].changeToStandart()
                self.ui.UsersButtonsScrollArea[k].setStandartColor()
            


    #Нажатие левой кнопки добвления нового фильтра пользователя
    def clkNameAddButton(self):
        def addButtonInScroll(name):
            #Проверяем есть ли уже такое имя и пустое ли поле
            if(name in self.ui.UsersButtonsScrollArea.keys() or len(name)==0 ):
                return False
            #Добавляем в БД
            addButtonNameToDB(name)

            self.ui.UsersButtonsScrollArea[name]=NameButton(self.ui,name)
            self.ui.verticalLayout_19.removeItem(self.spacerItem)
            self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.ui.verticalLayout_19.addItem(self.spacerItem)
            self.ui.selectName.addItem(name)

            return True

        #Ошибка если поле пустое или имя повторяется
        if(not addButtonInScroll(self.ui.lineEditName.text())):
            self.ui.lineEditName.setPlaceholderText("Ошибка ввода")
        else:
            self.ui.lineEditName.setPlaceholderText("Введите имя пользователя")
        self.ui.lineEditName.setText("")

    #Правая кнопка добавления новой записи
    def clkItemAddButton(self):
        
        def addItem(name,text,data,startTime,endTime,everyWeek=False,addToCalendar=False):
            if(str(endTime)<str(startTime)):
                return False
            Item=NoteItemData(name,text,data,startTime,endTime,everyWeek,addToCalendar)
            self.ui.NoteItemsUI.addItem(Item)
            self.ui.NoteItemsUI.Drow(name)
            addItemToDB(Item)
            return True

        text=self.ui.enterText.toPlainText()
        name=self.ui.selectName.currentText()
        self.ui.enterText.setPlainText('')
        startTime=self.ui.startTime.time().toString()

        endTime=self.ui.endTime.time().toString()
        data=self.ui.selectDate.date().toString()
        if(addItem(name,text,data,startTime,endTime,self.ui.checkBox.isChecked(),self.ui.addToKal.isChecked())):
            self.ui.enterText.setPlaceholderText('Место для вашей заметки')
        else:
            self.ui.enterText.setPlaceholderText('Ошибка. Некоректный интервал времени.')

    def setDefCalendar(self):
        self.ui.dateEdit_2.setVisible(False)
        self.ui.textEdit_2.setVisible(False)
        self.ui.textEdit_3.setVisible(False)

        self.ui.textEdit.setVisible(False)
        self.ui.textEdit_8.setVisible(False)
        self.ui.textEdit_9.setVisible(False)
        self.ui.textEdit_10.setVisible(False)

        self.ui.textEdit_14.setVisible(False)
        self.ui.textEdit_15.setVisible(False)
        self.ui.textEdit_16.setVisible(False)

        self.ui.textEdit_11.setVisible(False)
        self.ui.textEdit_12.setVisible(False)
        self.ui.textEdit_13.setVisible(False)
        #today+=timedelta(days=1)
        

if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   w = MWidget()
   w.setWindowTitle('Tutor Assistant')
   w.setWindowIcon(QtGui.QIcon('Icon.ico'))
   w.show()
   sys.exit(app.exec_())