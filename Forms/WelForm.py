# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NACHALNOE.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(460, 523)
        Form.setStyleSheet("background-color: rgb(32, 34, 37);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("font: 75 10pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(54, 57, 63);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setMinimumSize(QtCore.QSize(250, 100))
        self.pushButton_2.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(54, 57, 63);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(374, 261))
        self.label_2.setMaximumSize(QtCore.QSize(374, 261))
        self.label_2.setStyleSheet("font: 29pt \"MS Shell Dlg 2\";\n"
"\n"
"color: rgb(191, 191, 191);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Справка"))
        self.pushButton.setText(_translate("Form", "?"))
        self.pushButton_2.setText(_translate("Form", "Запуск"))
        self.label_2.setText(_translate("Form", "TutorAssistant "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
