# -*- coding: utf-8 -*-

import glob, os
import sys, shutil
import datetime, subprocess
from datetime import datetime, timedelta
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidgetItem, QDateTimeEdit, QMessageBox
from PyQt5.QtCore import QDate, QTime, QDateTime
 
from GUI import Ui_MainWindow
import sys

sysavg = []


class mywindow(QtWidgets.QMainWindow):
    source = ""
    target = ""

    CURENT = 0
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setAcceptDrops(True)
        #print(app.arguments())
        mywindow.source = app.arguments()[1]
        #self.ui.comboBox.addItem(app.arguments()[1])
        mywindow.target = r"\\192.168.1.170\мах"
        self.statusBar().showMessage(mywindow.target + " to " + mywindow.source)
        self.ui.Send.clicked.connect(self.SendF)

        self.ui.Cancel.clicked.connect(self.CancelF)


    def SendF(self):      
        
        #proc = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #proc.wait()
        #res = proc.communicate()
        #shutil.copy(mywindow.source.replace('\\','\\'), mywindow.target.replace('\\','\\'))
        
        #self.statusBar().showMessage(mywindow.source + " to " + mywindow.target )
        try:
            os.system('C:\\Windows\\robocopy.exe /y "{source}" "{target}" > nul'.format(source=mywindow.source, target=mywindow.target))
            #proc = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except IOError as e:
            print("Unable to copy file. %s" % e)
            exit(1)
        except:
            print("Unexpected error:", sys.exc_info())
            exit(1)
        #
        self.statusBar().showMessage("oooo")
    
    def CancelF(self):
        print("Exit")
        sys.exit()
        
app = QtWidgets.QApplication(sys.argv)
application = mywindow()
sysavg = app.arguments()
application.show()
 
sys.exit(app.exec())
