# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 56)
        MainWindow.setMinimumSize(QtCore.QSize(554, 56))
        MainWindow.setMaximumSize(QtCore.QSize(554, 56))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Windows/Cursors/lnesw.cur"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 351, 22))
        self.comboBox.setObjectName("comboBox")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Windows/Cursors/aero_ew_l.cur"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.comboBox.addItem(icon1, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.Send = QtWidgets.QPushButton(self.centralwidget)
        self.Send.setGeometry(QtCore.QRect(370, 10, 75, 23))
        self.Send.setObjectName("Send")
        self.Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel.setGeometry(QtCore.QRect(450, 10, 75, 23))
        self.Cancel.setObjectName("Cancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSend = QtWidgets.QAction(MainWindow)
        self.actionSend.setObjectName("actionSend")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Копирование на VPlay"))
        self.comboBox.setItemText(0, _translate("MainWindow", "МЕЖПРОГРАММКА"))
        self.comboBox.setItemText(1, _translate("MainWindow", "СОБСТВЕННЫЕ"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ПРОМО"))
        self.comboBox.setItemText(3, _translate("MainWindow", "ТЕМР"))
        self.Send.setText(_translate("MainWindow", "OK"))
        self.Cancel.setText(_translate("MainWindow", "Отмена"))
        self.actionSend.setText(_translate("MainWindow", "Send"))
