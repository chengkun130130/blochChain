# ui 组件
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QStringListModel 
from PyQt5.QtWidgets import   QMessageBox,QListView, QStatusBar,  QMenuBar,QMenu,QAction,QLineEdit,QStyle,QFormLayout,   QVBoxLayout,QWidget,QApplication ,QHBoxLayout, QPushButton,QMainWindow,QGridLayout,QLabel
from PyQt5.QtGui import QIcon,QPixmap,QStandardItem,QStandardItemModel
from PyQt5.QtCore import QStringListModel,QAbstractListModel,QModelIndex,QSize
# 模拟按键
import pymouse,pykeyboard,os,sys
from pymouse import *
from pykeyboard import PyKeyboard

import tkinter as tk
from PIL import ImageGrab
from aip import AipOcr
import pyautogui,time,sys
# import  pymssql
import pymysql
# 数据库连接设置
hostVal="rm-bp1b7b8guumr51js9oo.mysql.rds.aliyuncs.com"
portVal=3306
userVal="my_python"
passwdVal="1qaz2wsx@"
dbVal="my_python"

getSql1 = "SELECT ZH,JSBH,DJT FROM account order by id desc"#查询第一台机器使用的账号
# m 鼠标操作 k键盘操作
m = PyMouse()
k = PyKeyboard()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 901)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 321, 650))
        self.listWidget.setObjectName("listWidget")

        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        desktop = QApplication.desktop()
        # 通过桌面的宽和高来比例位置显示
        Dialog.move(desktop.width()*1-320, desktop.height()*0)
        
        for num in range(0,1000):
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)


        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 850, 60, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 850, 75, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 850, 75, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 850, 60, 41))
        self.pushButton_4.setObjectName("pushButton_3")

        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 660, 50, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(80, 660, 230, 31))
        self.textEdit.setObjectName("textEdit")

        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 700, 50, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(80, 700, 230, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 740, 50, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(80, 740, 230, 31))
        self.textEdit_3.setObjectName("textEdit_3")

        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 780, 50, 31))
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 820, 50, 31))
        self.pushButton_9.setStyleSheet("color:rgb(255,0,0)")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(12)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")

        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(80, 780, 230, 31))
        self.textEdit_4.setObjectName("textEdit_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setUser(self):
        ZHVal = self.textEdit.toPlainText()
        MMVal = "z12345678"
        JQBHVal = self.textEdit_2.toPlainText()+"号机"
        JSBHVal = self.textEdit_3.toPlainText()
        ISYXVal = "是"
        PLZVal = 12
        LCBHVal = self.textEdit_4.toPlainText()
        DJTVal = "1"

        connSet= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
        curSet = connSet.cursor()
        sql = "INSERT INTO account(ZH, MM,JQBH,JSBH,ISYX,PLZ,LCBH,DJT)\
         VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" %(ZHVal, MMVal, JQBHVal ,JSBHVal ,ISYXVal ,PLZVal,LCBHVal,DJTVal)
        try:
            curSet.execute(sql)
            connSet.commit()
        except:
            connSet.rollback()

        MainWindow = QMainWindow()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Dialog", "Dialog"))
        self.view1=[]
        connSelect= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
        curSelect = connSelect.cursor()
        curSelect.execute(getSql1)
        self.view1=curSelect.fetchall()
        # 第一个显示格子
        __sortingEnabled = self.listWidget.isSortingEnabled()
        for num in range(0,100):
            # strVal = self.view1[i1][0]+"@"+self.view1[i1][1]
            item = self.listWidget.item(num)
            item.setText(_translate("Dialog", ""))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        for i1 in range(len(self.view1)):
            strVal = self.view1[i1][0]+"@"+self.view1[i1][1]
            item = self.listWidget.item(i1)
            item.setText(_translate("Dialog", strVal))
        self.listWidget.setSortingEnabled(__sortingEnabled)       
    
    def delUser(self):
        try:
            selectAcc = self.listWidget.selectedItems()
            strlist = selectAcc[0].text().split('@')
            deleteSql = "DELETE  FROM  account WHERE ZH ='"+strlist[0]+"'"
            connDelete= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
            curDelete = connDelete.cursor()
            curDelete.execute(deleteSql)
            connDelete.commit()
            connDelete.close()
            
            
            MainWindow = QMainWindow()
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("Dialog", "Dialog"))
            self.view1=[]
            connSelect= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
            curSelect = connSelect.cursor()
            curSelect.execute(getSql1)
            self.view1=curSelect.fetchall()
            # 第一个显示格子
            __sortingEnabled = self.listWidget.isSortingEnabled()
            for num in range(0,100):
                # strVal = self.view1[i1][0]+"@"+self.view1[i1][1]
                item = self.listWidget.item(num)
                item.setText(_translate("Dialog", ""))
            self.listWidget.setSortingEnabled(__sortingEnabled)
            __sortingEnabled = self.listWidget.isSortingEnabled()
            self.listWidget.setSortingEnabled(False)
            for i1 in range(len(self.view1)):
                strVal = self.view1[i1][0]+"@"+self.view1[i1][1]
                item = self.listWidget.item(i1)
                item.setText(_translate("Dialog", strVal))
            self.listWidget.setSortingEnabled(__sortingEnabled)
             
        except:
            print("错误") 

    def delJsUser(self):
        try:
            selectAcc = self.listWidget.selectedItems()
            strlist = selectAcc[0].text().split('@')
            deleteSql = "DELETE  FROM  account WHERE ZH ='"+strlist[0]+"' and JSBH = '"+strlist[1]+"'"
            connDelete= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
            curDelete = connDelete.cursor()
            curDelete.execute(deleteSql)
            connDelete.commit()
            connDelete.close()
            
            
            MainWindow = QMainWindow()
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("Dialog", "Dialog"))
            self.view1=[]
            connSelect= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
            curSelect = connSelect.cursor()
            curSelect.execute(getSql1)
            self.view1=curSelect.fetchall()
            # 第一个显示格子
            __sortingEnabled = self.listWidget.isSortingEnabled()
            for num in range(0,100):
                # strVal = self.view1[i1][0]+"@"+self.view1[i1][1]
                item = self.listWidget.item(num)
                item.setText(_translate("Dialog", ""))
            self.listWidget.setSortingEnabled(__sortingEnabled)
            __sortingEnabled = self.listWidget.isSortingEnabled()
            self.listWidget.setSortingEnabled(False)
            for i1 in range(len(self.view1)):
                strVal = self.view1[i1][0]+"@"+self.view1[i1][1]
                item = self.listWidget.item(i1)
                item.setText(_translate("Dialog", strVal))
            self.listWidget.setSortingEnabled(__sortingEnabled)
             
        except:
            print("错误")
    def selUser(self):
        JQBHVal = self.textEdit_2.toPlainText()
        DJTVal = self.textEdit_4.toPlainText()
        if(JQBHVal!="" and DJTVal != ""):
            JQBHVal = JQBHVal+"号机"
            selectSql = "SELECT ZH,JSBH,DJT FROM account where JQBH = '"+JQBHVal+"' AND LCBH = '"+DJTVal+"' order by id desc"
        elif(JQBHVal!="" and DJTVal == ""):
            JQBHVal = JQBHVal+"号机"
            selectSql = "SELECT ZH,JSBH,DJT FROM account where JQBH = '"+JQBHVal+"' order by id desc"
        elif(JQBHVal=="" and DJTVal != ""):
            selectSql = "SELECT ZH,JSBH,DJT FROM account where LCBH = '"+DJTVal+"' order by id desc"
        else:
            selectSql = "SELECT ZH,JSBH,DJT FROM account order by id desc"
        print(JQBHVal)
        print(selectSql)
        print("查询角色")
        MainWindow = QMainWindow()
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Dialog", "Dialog"))
        self.view1=[]
        connSelect= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
        curSelect = connSelect.cursor()
        curSelect.execute(selectSql)
        self.view1=curSelect.fetchall()
        print(self.view1)
        # print(self.view1)
        # 第一个显示格子
        __sortingEnabled = self.listWidget.isSortingEnabled()
        for num in range(0,100):
            item = self.listWidget.item(num)
            item.setText(_translate("Dialog", ""))
        self.listWidget.setSortingEnabled(__sortingEnabled)

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        for i1 in range(len(self.view1)):
            strVal = self.view1[i1][0]+"@"+self.view1[i1][1]+"@"+self.view1[i1][2]
            item = self.listWidget.item(i1)
            item.setText(_translate("Dialog", strVal))
        self.listWidget.setSortingEnabled(__sortingEnabled)   
        # 初始化
    def inI(self):
        switchSelSql = "SELECT id,ZH,JSBH,PLZ FROM account WHERE PLZ < '12'"
        connSelect= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
        curSelect = connSelect.cursor()
        curSelect.execute(switchSelSql)
        val = curSelect.fetchall()
        for index in range(len(val)):
            if(int(val[index][3]) + 4 >= 12 ):
                PLZVal = 12
                print(int(val[index][0]))
                switchSql = "UPDATE account SET PLZ = "+str(PLZVal)+" WHERE ZH = '"+val[index][1]+"' AND JSBH = '"+val[index][2]+"'"
                curSelect.execute(switchSql)
                connSelect.commit()
                # connSelect.close()
            elif(int(val[index][3]) + 4 < 12):
                PLZVal = val[index][3]+4
                switchSql = "UPDATE account SET PLZ = "+str(PLZVal)+" WHERE ZH = '"+val[index][1]+"' AND JSBH = '"+val[index][2]+"'"
                curSelect.execute(switchSql)
                connSelect.commit() 
        connSelect.close()   
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.view1=[]
        connSelect= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
        curSelect = connSelect.cursor()
        curSelect.execute(getSql1)
        self.view1=curSelect.fetchall()
        # 第一个显示格子
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        for i1 in range(len(self.view1)):
            strVal = self.view1[i1][0]+"@"+self.view1[i1][1]+"@"+self.view1[i1][2]
            item = self.listWidget.item(i1)
            item.setText(_translate("Dialog", strVal))
        self.listWidget.setSortingEnabled(__sortingEnabled)

        
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Dialog", "存入"))
        self.pushButton.clicked.connect(self.setUser)

        self.pushButton_2.setText(_translate("Dialog", "删除账号"))
        self.pushButton_2.clicked.connect(self.delUser)

        self.pushButton_3.setText(_translate("Dialog", "删除角色"))
        self.pushButton_3.clicked.connect(self.delJsUser)

        self.pushButton_4.setText(_translate("Dialog", "查询"))
        self.pushButton_4.clicked.connect(self.selUser)

        self.pushButton_9.setText(_translate("Dialog", "初始化"))
        self.pushButton_9.clicked.connect(self.inI)

        self.pushButton_5.setText(_translate("Dialog", "账号"))
        self.pushButton_6.setText(_translate("Dialog", "机器号"))
        self.pushButton_7.setText(_translate("Dialog", "角色"))
        self.pushButton_8.setText(_translate("Dialog", "编组"))
        
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())