# ui 组件
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QStringListModel 
from PyQt5.QtWidgets import   QMessageBox,QListView, QStatusBar,  QMenuBar,QMenu,QAction,QLineEdit,QStyle,QFormLayout,   QVBoxLayout,QWidget,QApplication ,QHBoxLayout, QPushButton,QMainWindow,QGridLayout,QLabel
from PyQt5.QtGui import QIcon,QPixmap,QStandardItem,QStandardItemModel
from PyQt5.QtCore import QStringListModel,QAbstractListModel,QModelIndex,QSize
import random
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
# 百度识图账户信息
# APP_ID = '18671135'
# API_KEY = 'k2YWlrlg14PXGBA2RE9ede9O'
# SECRET_KEY = 'vClNwl9OME8yIrG8Q5VuqK04q6EAA2mv'

APP_ID = '20396492'
API_KEY = 'RVO4b6fBqefILMnebAa2932A'
SECRET_KEY = '8Vom46kx0LeIKgnSlsiEeKUIcpeIOGhB'

# APP_ID = '20519560'
# API_KEY = 'NCgMWWNXGzctw2M96zGr1XeS'
# SECRET_KEY = 'czrq5C8esXEd0MnkT7uDXBZnwUURtVCu'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
window = tk.Tk()
window.title('新建文本文档')
window.geometry('400x800+1300+100')
filePath = r"D:\DNweituo.png"
# 数据库连接参数
hostVal="rm-bp1b7b8guumr51js9oo.mysql.rds.aliyuncs.com"
portVal=3306
userVal="my_python"
passwdVal="1qaz2wsx@"
dbVal="my_python"
# 本地连接
# hostVal="127.0.0.1"
# portVal=3306
# userVal="root"
# passwdVal="1qaz2wsx@"
# dbVal="python"

m = PyMouse()
k = PyKeyboard()

# 截图
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
class Ui_Dialog(object):
    JQBHVal = "10号机"
    XSPMVal = "1"
    DWBHVal = "3"
    ZHVal = ""
    JSBHVal = ""
    RWMCVal = ""
    RWBMVal = ""
    RWSZVal = 1
    LCBHVal = ""
    RMSL = 0
    DJTVal = 1
    LCBHUserVal = "A"
    # PLZZH = ""
    # 查看的sql
    view1=[]
    view2=[]
    view3=[]
    view4=[]
    view5=[]
    getSql1 = "SELECT DISTINCT RWMC FROM taskdata where DWBH = '1'"#查询编队为5的任务 更改数字更改编队
    getSql2 = "SELECT DISTINCT RWMC FROM taskdata where DWBH = '2'"#查询编队为6的任务 更改数字更改编队 
    getSql3 = "SELECT DISTINCT RWMC FROM taskdata where DWBH = '3'"#查询编队为7的任务 更改数字更改编队
    getSql4 = "SELECT DISTINCT RWMC FROM taskdata where DWBH = '4'"#查询编队为8的任务 更改数字更改编队
    # 清除sql
    deleteSql = "DELETE  FROM  taskdata WHERE XSPM ='1'"

    deleteUserSql = "DELETE  FROM  logouser WHERE XSPM ='1'"
    # 插入数据
    def setVal(self):
        connSet= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
        connSet.ping(reconnect=True) 
        curSet = connSet.cursor()
        if(self.ZHVal == ""):
            print("没选择账号")
            return
        if(self.JSBHVal == ""):
            print("没选择角色")
            return          
        sql = "INSERT INTO taskdata(JQBH, XSPM,ZH,JSBH,RWMC,RWBM,DWBH,RWSZ,LCBH)\
            VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(self.JQBHVal, self.XSPMVal, self.ZHVal, self.JSBHVal ,self.RWMCVal,self.RWBMVal,self.DWBHVal,self.RWSZVal,self.LCBHVal)
        try:    
            # selectTask = ""
            curSet.execute(sql)
            connSet.commit()
            connSet.close()
            return True
        except:
            connSet.rollback()
            return True
    # 截图写入数据
    def catch(self):
        img=ImageGrab.grab(bbox=(580,400,1020,480))
        img.save(filePath)
        image = get_file_content(filePath)
        req = client.basicGeneral(image)
        all_test =''
        for i in req['words_result']:
            all_test += i['words']
        if (all_test==""):
            all_test="没有截取可用数据!"    
        sheet = ['传说中的魔兽','渔夫的生活',"不是胆小鬼","胜负","查尔德不是孩子","消失的名字","勇士之路","永恒的美丽","快速侦察"]
        all_test = all_test.replace('!','')
        abscissa = random.randint(780, 830)
        abscissaFalse = random.randint(930, 960)
        slidingTime = random.uniform(0.1, 0.5)
        if(all_test in sheet):
            if(all_test=='传说中的魔兽'):
                all_test="狮蝎巢穴"            
                self.RWMCVal="狮蝎巢穴"   
                self.RWBMVal = "A"         
            elif(all_test=="渔夫的生活"):
                all_test="卡伊伦巢穴"
                self.RWMCVal="卡伊伦巢穴" 
                self.RWBMVal = "B"    
            elif(all_test=="不是胆小鬼"):
                all_test="大主教巢穴"
                self.RWMCVal="大主教巢穴"
                self.RWBMVal = "C"     
            elif(all_test=="胜负"):
                all_test="K博士巢穴"
                self.RWMCVal="K博士巢穴" 
                self.RWBMVal = "D"    
            elif(all_test=="查尔德不是孩子"):
                all_test="代达罗斯巢穴"
                self.RWMCVal="代达罗斯巢穴"
                self.RWBMVal = "E"     
            elif(all_test=="消失的名字"):
                all_test="格拉诺巢穴"
                self.RWMCVal="格拉诺巢穴"
                self.RWBMVal = "F"     
            elif(all_test=="勇士之路"):
                all_test="火山巢穴"
                self.RWMCVal="火山巢穴"  
                self.RWBMVal = "G"
            elif(all_test == "快速侦察"):
                all_test="台风金巢穴"
                self.RWMCVal="台风金巢穴"  
                self.RWBMVal = "H"
            elif(all_test == "永恒的美丽"):
                all_test="守卫者巢穴"
                self.RWMCVal="守卫者巢穴"  
                self.RWBMVal = "I"     
            pyautogui.moveTo(abscissaFalse,560,duration=slidingTime)
            pyautogui.click(abscissaFalse,560)
            if(self.setVal()):
                return True                      
        elif("逆袭" in all_test):
            self.RWMCVal = all_test
            self.RWBMVal = "sssss"
            # self.setVal()
            pyautogui.moveTo(abscissaFalse,560,duration=slidingTime)
            pyautogui.click(abscissaFalse,560)
            if(self.setVal()):
                return True
        else:
            pyautogui.moveTo(abscissa,560,duration=slidingTime)
            pyautogui.click(abscissa,560)
            return True           
    # 创建window
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 1000)

        # 通过桌面的宽和高来比例位置显示
        desktop = QApplication.desktop()
        Dialog.move(desktop.width()*1-320, desktop.height()*0)

        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 271, 301))
        self.listWidget.setObjectName("listWidget")
        for num in range(0,1000):
            item = QtWidgets.QListWidgetItem()  
            item = QtWidgets.QListWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(14)
            item.setFont(font)
            self.listWidget.addItem(item)
        self.listWidget.itemClicked.connect(self.ClickBtn)

        self.listWidget_3 = QtWidgets.QListWidget(Dialog)
        self.listWidget_3.setGeometry(QtCore.QRect(0, 300, 281, 101))
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.listWidget_3.addItem(item)
        self.listWidget_3.itemClicked.connect(self.ClickBtn2)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 0, 50, 52))
        self.pushButton.setStyleSheet("color:rgb(0,0,255)")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(25)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 50, 50, 52))
        self.pushButton_2.setStyleSheet("color:rgb(0,0,255)")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(25)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 100, 50, 52))
        self.pushButton_3.setStyleSheet("color:rgb(0,0,255)")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(25)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 150, 50, 52))
        self.pushButton_4.setStyleSheet("color:rgb(0,0,255)")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(25)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 200, 50, 52))
        self.pushButton_5.setStyleSheet("color:rgb(255,0,0)")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(25)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(270, 250, 50, 52))
        self.pushButton_11.setStyleSheet("color:rgb(255,0,0)")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(25)
        font.setWeight(50)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(270, 300, 50, 52))
        self.pushButton_12.setStyleSheet("color:rgb(255,0,0)")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(25)
        font.setWeight(50)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")

        self.pushButton_13 = QtWidgets.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(270, 350, 50, 52))
        self.pushButton_13.setStyleSheet("color:rgb(255,0,0)")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(25)
        font.setWeight(50)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")


        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 400, 56, 51))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(55, 400, 56, 51))
        self.pushButton_14.setObjectName("pushButton_14")

        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(110, 400, 56, 51))
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(165, 400, 56, 51))
        self.pushButton_10.setObjectName("pushButton_10")

        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(220, 400, 56, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(275, 400, 56, 51))
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(0, 460, 56, 51))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(55, 460, 56, 51))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(Dialog)
        self.pushButton_17.setGeometry(QtCore.QRect(110, 460, 56, 51))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(Dialog)
        self.pushButton_18.setGeometry(QtCore.QRect(165, 460, 56, 51))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(Dialog)
        self.pushButton_19.setGeometry(QtCore.QRect(220, 460, 56, 51))
        self.pushButton_19.setStyleSheet("color:rgb(255,0,0)")
        font = QtGui.QFont()
        font.setFamily('微软雅黑')
        font.setBold(True)
        font.setPointSize(12)
        font.setWeight(50)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_1")
        self.pushButton_20 = QtWidgets.QPushButton(Dialog)
        self.pushButton_20.setGeometry(QtCore.QRect(275, 460, 56, 51))
        self.pushButton_20.setObjectName("pushButton_20")
        

        self.listWidget_2 = QtWidgets.QListWidget(Dialog)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 510, 319, 540))
        self.listWidget_2.setObjectName("listWidget_2")
        # K博士 
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        # 狮蝎 
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        # 大主教
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        # 格拉诺巢穴
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        # 卡伊伦巢穴
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        # 代达罗斯巢穴
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        # 火山巢穴
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        # 守卫
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        # 台风
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        # 逆袭
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(22)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget_2.addItem(item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    # 获取用户信息
    def getAccount(self,page0):
        connSelect= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
        curSelect = connSelect.cursor()
        try:          
            MainWindow = QMainWindow()
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("Dialog", "Dialog"))
            self.view1=[]
            if(self.DJTVal == 1):
                # sqlSelectCccount = "select ZH,JSBH from account where JQBH = '"+self.JQBHVal+"' and LCBH = 'A' and DJT = '"+DJTVal+"'  limit "+page0+",100"
                sqlSelectCccount = "SELECT ZH,JSBH FROM account WHERE PLZ <= '12' AND PLZ >= '8' and JQBH = '"+self.JQBHVal+"' AND LCBH = '"+self.LCBHUserVal+"'"
                curSelect.execute(sqlSelectCccount)
                self.view1= curSelect.fetchall()
            elif(self.DJTVal == 2):
                sqlSelectCccount = "SELECT ZH,JSBH FROM account WHERE PLZ < '8' AND PLZ >= '4' and JQBH = '"+self.JQBHVal+"' AND LCBH = '"+self.LCBHUserVal+"'"
                curSelect.execute(sqlSelectCccount)
                self.view1= curSelect.fetchall()
            elif(self.DJTVal == 3):
                sqlSelectCccount = "SELECT ZH,JSBH FROM account WHERE PLZ < '4' AND PLZ > '0' and JQBH = '"+self.JQBHVal+"' AND LCBH = '"+self.LCBHUserVal+"'"
                curSelect.execute(sqlSelectCccount)
                self.view1= curSelect.fetchall() 
            elif(self.DJTVal == 4):
                sqlSelectCccount = "SELECT ZH,JSBH FROM account WHERE PLZ = '0' and JQBH = '"+self.JQBHVal+"' AND LCBH = '"+self.LCBHUserVal+"'"
                curSelect.execute(sqlSelectCccount)
                self.view1= curSelect.fetchall()  
            # 第一个显示格子
            __sortingEnabled = self.listWidget.isSortingEnabled()
            self.listWidget.setSortingEnabled(False)
            for num in range(0,1000):
                item = self.listWidget.item(num)
                item.setText(_translate("Dialog", ""))
            self.listWidget.setSortingEnabled(__sortingEnabled) 
            
            __sortingEnabled = self.listWidget.isSortingEnabled()
            self.listWidget.setSortingEnabled(False)
            for i1 in range(len(self.view1)):
                showIndex = str(i1+1)
                item = self.listWidget.item(i1)
                showView =showIndex+"@"+self.view1[i1][0]+"@"+self.view1[i1][1]
                item.setText(_translate("Dialog", showView))
            self.listWidget.setSortingEnabled(__sortingEnabled)   
        except :
            connSelect.rollback() 
    # def getAccountB(self,page0):
    #     connSelect= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
    #     curSelect = connSelect.cursor()
    #     try:          
    #         MainWindow = QMainWindow()
    #         _translate = QtCore.QCoreApplication.translate
    #         MainWindow.setWindowTitle(_translate("Dialog", "Dialog"))
    #         self.view1=[]
    #         sqlSelectCccount = "select ZH,JSBH from account where JQBH = '"+self.JQBHVal+"' and LCBH = 'B' limit "+page0+",100"
    #         curSelect.execute(sqlSelectCccount)
    #         self.view1= curSelect.fetchall()
    #         # 第一个显示格子
    #         __sortingEnabled = self.listWidget.isSortingEnabled()
    #         self.listWidget.setSortingEnabled(False)
    #         for num in range(0,50):
    #             item = self.listWidget.item(num)
    #             item.setText(_translate("Dialog", ""))
    #         self.listWidget.setSortingEnabled(__sortingEnabled)   
    #         __sortingEnabled = self.listWidget.isSortingEnabled()
    #         self.listWidget.setSortingEnabled(False)
    #         for i1 in range(len(self.view1)):
    #             showIndex = str(i1+1)
    #             item = self.listWidget.item(i1)
    #             showView =showIndex+"@"+ self.view1[i1][0]+"@"+self.view1[i1][1]
    #             item.setText(_translate("Dialog", showView))
    #         self.listWidget.setSortingEnabled(__sortingEnabled)   
    #     except :
    #         connSelect.rollback()
    # 登录
    def loginSelect(self):
        try:
            # selectAcc = self.listWidget.selectedItems()
            # strlist = selectAcc[0].text().split('@')
            sqlPassword = "SELECT ZH,MM,JSBH FROM account WHERE ZH = '"+self.ZHVal+"' AND JSBH = '"+self.JSBHVal+"'"
            connSelect= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
            curSelect = connSelect.cursor()
            curSelect.execute(sqlPassword)
            val = curSelect.fetchall()
            sqlSetZH = "INSERT INTO logouser(ZH, JQBH,LCBH,JSBH,XSPM)\
            VALUES('%s','%s','%s','%s','%s')" %(self.ZHVal,self.JQBHVal,self.LCBHVal,self.JSBHVal,self.XSPMVal)
            curSelect.execute(sqlSetZH)
            connSelect.commit()
            connSelect.close()
            m.click(1430, 520)
            time.sleep(0.5)
            m.click(1430, 520)
            m.click(1430, 520)
            time.sleep(0.5)
            k.tap_key(k.delete_key,20) 
            time.sleep(0.5)
            k.type_string(val[0][0])
            time.sleep(0.5)
            m.click(1430, 560)
            time.sleep(0.5)
            k.type_string(val[0][1])
        except :
            print("错误")
    # 点击账号列表
    def ClickBtn(self):
        selectAcc = self.listWidget.selectedItems()
        
        strlist = selectAcc[0].text().split('@')
        print(strlist)
        if(strlist[0]!=""):
            self.LCBHVal = strlist[0]
            self.ZHVal = strlist[1]
            self.JSBHVal = strlist[2]
            print(self.LCBHVal)
            print(self.ZHVal)
            print(self.JSBHVal)
        else:
            self.LCBHVal = ""
            self.ZHVal = ""
            self.JSBHVal = ""
            print("请选择有效账号")
    # 点击最优账号
    def ClickBtn2(self):
        selectAcc = self.listWidget_3.selectedItems()
        strlist = selectAcc[0].text().split('@')
        if(strlist[0]!=""):
            self.ZHVal = strlist[0]
            self.JSBHVal = strlist[1]
            self.LCBHVal = ""
        else:
            self.ZHVal = ""
            self.JSBHVal = ""
            self.LCBHVal = ""
            print("请选择有效账号")
    # 开始删选任务
    def startDelTask(self):
        if(self.ZHVal == ""):
            print("没选择账号")
            return
        if(self.JSBHVal == ""):
            print("没选择角色")
            return 
        abscissa = random.randint(335, 350)
        ordinate = random.randint(450, 465)
        slidingTime = random.uniform(0.1, 0.5)
        pyautogui.moveTo(abscissa,ordinate,duration=slidingTime)
        pyautogui.click(abscissa,ordinate)
        time.sleep(0.1)
        if(self.catch()):
            abscissa = random.randint(565, 575)
            ordinate = random.randint(325, 335)
            pyautogui.moveTo(abscissa,ordinate,duration=slidingTime)
            pyautogui.click(abscissa,ordinate)
            time.sleep(0.1)
            if(self.catch()):
                abscissa = random.randint(735, 745)
                ordinate = random.randint(480, 490)
                pyautogui.moveTo(abscissa,ordinate,duration=slidingTime)
                pyautogui.click(abscissa,ordinate)
                time.sleep(0.1)
                if(self.catch()):
                    abscissa = random.randint(375, 385)
                    ordinate = random.randint(770, 780)
                    pyautogui.moveTo(abscissa,ordinate,duration=slidingTime)
                    pyautogui.click(abscissa,ordinate)
                    time.sleep(0.1)
                    if(self.catch()):
                        abscissa = random.randint(490, 500)
                        ordinate = random.randint(580, 590)
                        pyautogui.moveTo(abscissa,ordinate,duration=slidingTime)
                        pyautogui.click(abscissa,ordinate)
                        time.sleep(0.1)
                        if(self.catch()):
                            abscissa = random.randint(720, 730)
                            ordinate = random.randint(755, 765)
                            pyautogui.moveTo(abscissa,ordinate,duration=slidingTime)
                            pyautogui.click(abscissa,ordinate)
                            time.sleep(0.1)
                            self.catch()
    # 二次删除任务
    def delSql(self):
        img=ImageGrab.grab(bbox=(580,400,1020,480))
        img.save(filePath)
        image = get_file_content(filePath)
        req = client.basicGeneral(image)
        all_test =''
        for i in req['words_result']:
            all_test += i['words']
        all_test = all_test.replace('!','')
        if (all_test==""):
            all_test="没有截取可用数据"

        if(all_test=='传说中的魔兽'):
            all_test="狮蝎巢穴"            
        elif(all_test=="渔夫的生活"):
            all_test="卡伊伦巢穴"
        elif(all_test=="不是胆小鬼"):
            all_test="大主教巢穴"
        elif(all_test=="胜负"):
            all_test="K博士巢穴"
        elif(all_test=="查尔德不是孩子"):
            all_test="代达罗斯巢穴"
        elif(all_test=="消失的名字"):
            all_test="格拉诺巢穴"
        elif(all_test=="勇士之路"):
            all_test="火山巢穴"
        elif(all_test == "永恒的美丽"):
            all_test="守卫者巢穴"
        elif(all_test == "快速侦察"):
            all_test="台风金巢穴"

        connDelSql= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
        curDelSql = connDelSql.cursor()
        sqlDelRql="SELECT DISTINCT JQBH,RWMC FROM taskdata where RWMC = '"+all_test+"' and DWBH = '"+self.DWBHVal+"' AND LCBH = '"+self.LCBHVal+"'"
        curDelSql.execute(sqlDelRql)
        sqlDelRqlList=curDelSql.fetchall()
        connDelSql.close()

        abscissa = random.randint(780, 830)
        abscissaFalse = random.randint(930, 960)
        slidingTime = random.uniform(0.1, 0.5)
        if(len(sqlDelRqlList)>0):
            if(all_test==sqlDelRqlList[0][1] and self.JQBHVal == sqlDelRqlList[0][0]):
                pyautogui.moveTo(abscissaFalse,560,duration=slidingTime)
                pyautogui.click(abscissaFalse,560)
                print("是本机器")
                return True
            else:
                print("不是本机器")
                pyautogui.moveTo(abscissa,560,duration=slidingTime)
                pyautogui.click(abscissa,560)
                return True
        else:
            print("没查到相关数据")
            pyautogui.moveTo(abscissa,560,duration=slidingTime)
            pyautogui.click(abscissa,560)
            return True
    # 第二次筛选任务
    def againDelTask(self):
        abscissa = random.randint(335, 350)
        ordinate = random.randint(450, 465)
        pyautogui.moveTo(abscissa,ordinate,duration=1)
        pyautogui.click(abscissa,ordinate)
        time.sleep(0.1)
        if(self.delSql()):
            abscissa = random.randint(565, 575)
            ordinate = random.randint(325, 335)
            pyautogui.moveTo(abscissa,ordinate,duration=1)
            pyautogui.click(abscissa,ordinate)
            time.sleep(0.1)
            if(self.delSql()):
                abscissa = random.randint(735, 745)
                ordinate = random.randint(480, 490)
                pyautogui.moveTo(abscissa,ordinate,duration=1)
                pyautogui.click(abscissa,ordinate)
                time.sleep(0.1)
                if(self.delSql()):
                    abscissa = random.randint(375, 385)
                    ordinate = random.randint(770, 780)
                    pyautogui.moveTo(abscissa,ordinate,duration=1)
                    pyautogui.click(abscissa,ordinate)
                    time.sleep(0.1)
                    if(self.delSql()):
                        abscissa = random.randint(490, 500)
                        ordinate = random.randint(580, 590)
                        pyautogui.moveTo(abscissa,ordinate,duration=1)
                        pyautogui.click(abscissa,ordinate)
                        time.sleep(0.1)
                        if(self.delSql()):
                            abscissa = random.randint(720, 730)
                            ordinate = random.randint(755, 765)
                            pyautogui.moveTo(abscissa,ordinate,duration=1)
                            pyautogui.click(abscissa,ordinate)
                            time.sleep(0.1)
                            self.delSql() 
    # 进入频道
    def EnterClick(self):    
        transverse = random.randint(600, 1000)
        slidingTime = random.uniform(0.1, 0.5)
        if(self.JQBHVal == "1号机" or self.JQBHVal == "9号机"):
            pyautogui.moveTo(transverse,540,duration=slidingTime)
            pyautogui.click(transverse,540)
        elif(self.JQBHVal == "2号机" or self.JQBHVal == "10号机"):
            pyautogui.moveTo(transverse,570,duration=slidingTime)
            pyautogui.click(transverse,570)
        elif(self.JQBHVal == "3号机" or self.JQBHVal == "11号机"):
            pyautogui.moveTo(transverse,600,duration=slidingTime)
            pyautogui.click(transverse,600)
        elif(self.JQBHVal == "4号机" or self.JQBHVal == "12号机"):
            pyautogui.moveTo(transverse,630,duration=slidingTime)
            pyautogui.click(transverse,630)
        elif(self.JQBHVal == "5号机" or self.JQBHVal == "13号机"):
            pyautogui.moveTo(transverse,660,duration=slidingTime)
            pyautogui.click(transverse,660)
        elif(self.JQBHVal == "6号机" or self.JQBHVal == "14号机"):
            pyautogui.moveTo(transverse,690,duration=slidingTime)
            pyautogui.click(transverse,690)
        elif(self.JQBHVal == "7号机" or self.JQBHVal == "15号机"):
            pyautogui.moveTo(transverse,720,duration=slidingTime)
            pyautogui.click(transverse,720)
        elif(self.JQBHVal == "8号机" or self.JQBHVal == "16号机"):
            pyautogui.moveTo(transverse,750,duration=slidingTime)
            pyautogui.click(transverse,750)
    # 选择角色
    def selectRole(self):
        transverse = random.randint(1450, 1500)
        slidingTime = random.uniform(0.1, 0.5)
        if(self.JSBHVal == ""):
            print("请选择正确的账号角色")
            return
        elif(self.JSBHVal == "1"):
            ordinate = random.randint(220, 250)
            pyautogui.moveTo(transverse,ordinate,duration=slidingTime)
            pyautogui.click(transverse,ordinate)
        elif(self.JSBHVal == "2"):
            ordinate = random.randint(330, 340)
            pyautogui.moveTo(transverse,ordinate,duration=slidingTime)
            pyautogui.click(transverse,ordinate)
        elif(self.JSBHVal == "3"):
            ordinate = random.randint(420, 430)
            pyautogui.moveTo(transverse,ordinate,duration=slidingTime)
            pyautogui.click(transverse,ordinate)
        elif(self.JSBHVal == "4"):
            ordinate = random.randint(520, 530)
            pyautogui.moveTo(transverse,ordinate,duration=slidingTime)
            pyautogui.click(transverse,ordinate)
        elif(self.JSBHVal == "5"):
            ordinate = random.randint(620, 630)
            pyautogui.moveTo(transverse,ordinate,duration=slidingTime)
            pyautogui.click(transverse,ordinate)
        elif(self.JSBHVal == "5"):
            ordinate = random.randint(720, 730)
            pyautogui.moveTo(transverse,ordinate,duration=slidingTime)
            pyautogui.click(transverse,ordinate)
        else:
            print("请选择正确的账号角色")
    # 查看任务
    def showTask(self):   
        self.view1 = ["未查询"]  
        self.view2 = ["未查询"]  
        self.view3 = ["未查询"]  
        self.view4 = ["未查询"] 
        showView1=[]
        showView2=[]
        showView3=[]
        showView4=[]
        showName = []
        # try:
        MAXIndexSql = "SELECT LCBH FROM taskdata ORDER BY LCBH DESC LIMIT 1"
        connSelect= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
        curSelect = connSelect.cursor()
        curSelect.execute(MAXIndexSql)
        MaxIndexList=curSelect.fetchall()
        
        if(len(MaxIndexList)<1):
            MainWindow = QMainWindow()
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("Dialog", "Dialog")) 
            __sortingEnabled = self.listWidget_3.isSortingEnabled()
            self.listWidget_3.setSortingEnabled(False)
            item = self.listWidget_3.item(0)
            item.setText(_translate("Dialog",""))
            self.listWidget_3.setSortingEnabled(__sortingEnabled)

            __sortingEnabled = self.listWidget_2.isSortingEnabled()
            self.listWidget_2.setSortingEnabled(False)
            for index in range(0,13):
                item = self.listWidget_2.item(index)
                item.setText(_translate("Dialog",""))
            self.listWidget_2.setSortingEnabled(__sortingEnabled)
            print("没有数据")
            return
        MaxIndex = int(MaxIndexList[0][0])

        showTaskList1 = self.showMaxTask(MaxIndex,"1")
        self.view1 = showTaskList1[0]
        showTaskList2 = self.showMaxTask(MaxIndex,"2")
        self.view2 = showTaskList2[0]
        showTaskList3 = self.showMaxTask(MaxIndex,"3")
        self.view3 = showTaskList3[0]
        showTaskList4 = self.showMaxTask(MaxIndex,"4")
        self.view4 = showTaskList4[0]
        if(showTaskList1[1] and showTaskList2[1] and showTaskList3[1] and showTaskList4[1]):               
            if(len(self.view1)>0):
                for index1 in range(0,len(self.view1)):
                    showView1.append(self.view1[index1][3])
                    # if(self.view1[index1][0] == self.JQBHVal):
                    #     showName.append(self.view1[index1][1]+"@"+self.view1[index1][2])
            if(len(self.view2)>0):
                for index2 in range(0,len(self.view2)):
                    showView2.append(self.view2[index2][3])          
                    # if(self.view2[index2][0] == self.JQBHVal):
                    #     showName.append(self.view2[index2][1]+"@"+self.view2[index2][2])
            if(len(self.view3)>0):
                for index3 in range(0,len(self.view3)):
                    showView3.append(self.view3[index3][3])
                    # if(self.view3[index3][0] == self.JQBHVal):
                    #     showName.append(self.view3[index3][1]+"@"+self.view3[index3][2])
            if(len(self.view4)>0):
                for index4 in range(0,len(self.view4)):
                    showView4.append(self.view4[index4][3])
                    # if(self.view4[index4][0] == self.JQBHVal):
                    #     showName.append(self.view4[index4][1]+"@"+self.view4[index4][2])
            
            if(self.DWBHVal == "1"):
                selectLCBH = str(self.view1[0][4])
            elif(self.DWBHVal == "2"):
                selectLCBH = str(self.view2[0][4])
            elif(self.DWBHVal == "3"):
                selectLCBH = str(self.view3[0][4])
            elif(self.DWBHVal == "4"):
                selectLCBH = str(self.view4[0][4])
            print(selectLCBH)   
            sqlLog = "SELECT DISTINCT ZH,JQBH,JSBH,LCBH FROM logouser WHERE JQBH = '"+self.JQBHVal+"' AND LCBH = '"+selectLCBH+"'"
            curSelect.execute(sqlLog)
            showNameList = curSelect.fetchall()
            showName.append(showNameList[0][0]+"@"+showNameList[0][2])  
            # self.PLZZH = showNameList[0][0] 
            newNxList=[]
            if(len(showView1)!=0):
                i1 = 0
                while i1 < len(showView1):
                    if "逆袭" in showView1[i1]:
                        newNxList.append(showView1[i1])
                        showView1.pop(i1)
                        i1 -= 1
                    i1 += 1
            if(len(showView2)!=0):
                i2 = 0
                while i2 < len(showView2):
                    if "逆袭" in showView2[i2]:
                        newNxList.append(showView2[i2])
                        showView2.pop(i2)
                        i2 -= 1
                    i2 += 1
            if(len(showView3)!=0):
                i3 = 0
                while i3 < len(showView3):
                    if "逆袭" in showView3[i3]:
                        newNxList.append(showView3[i3])
                        showView3.pop(i3)
                        i3 -= 1
                    i3 += 1
            if(len(showView4)!=0):
                i4 = 0
                while i4 < len(showView4):
                    if "逆袭" in showView4[i4]:
                        newNxList.append(showView4[i4])
                        showView4.pop(i4)
                        i4 -= 1
                    i4 += 1
            if(len(showView1)!=0):
                newList=showView1
            if(len(showView2)!=0):
                if(len(newList)==0):
                    newList=showView2
                else:
                    newList=list(set(newList).intersection(set(showView2)))
            if(len(showView3)!=0):
                if(len(showView1)==0 and len(showView2)==0):
                    newList=showView3
                else:
                    newList=list(set(newList).intersection(set(showView3)))
            if(len(showView4)!=0):
                if(len(showView1)==0 and len(showView2)==0 and len(showView3)==0):
                    newList=showView4
                else:
                    newList=list(set(newList).intersection(set(showView4)))
            newNxList = list(set(newNxList))
            connSelect.close()
            self.view5=newList
            self.RMSL = len(self.view5)
            print(self.view5)
            MainWindow = QMainWindow()
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("Dialog", "Dialog"))                
            # 显示最佳账号
            if(len(showName)>=1):
                __sortingEnabled = self.listWidget_3.isSortingEnabled()
                self.listWidget_3.setSortingEnabled(False)
                item = self.listWidget_3.item(0)
                item.setText(_translate("Dialog", showName[0]))
                self.listWidget_3.setSortingEnabled(__sortingEnabled)
            # 显示任务
            __sortingEnabled = self.listWidget_2.isSortingEnabled()
            self.listWidget_2.setSortingEnabled(False)
            if ("K博士巢穴" in self.view5):
                item = self.listWidget_2.item(0)
                item.setText(_translate("Dialog", "K博士巢穴"))
            else:
                item = self.listWidget_2.item(0)
                item.setText(_translate("Dialog", ""))

            if("狮蝎巢穴" in self.view5):
                item = self.listWidget_2.item(1)
                item.setText(_translate("Dialog", "狮蝎巢穴"))
            else:
                item = self.listWidget_2.item(1)
                item.setText(_translate("Dialog", ""))

            if("大主教巢穴" in self.view5):
                item = self.listWidget_2.item(2)
                item.setText(_translate("Dialog", "大主教巢穴"))
            else:
                item = self.listWidget_2.item(2)
                item.setText(_translate("Dialog", ""))

            if("格拉诺巢穴" in self.view5):
                item = self.listWidget_2.item(3)
                item.setText(_translate("Dialog", "格拉诺巢穴"))
            else:
                item = self.listWidget_2.item(3)
                item.setText(_translate("Dialog", ""))

            if("卡伊伦巢穴" in self.view5):
                item = self.listWidget_2.item(4)
                item.setText(_translate("Dialog", "卡伊伦巢穴"))
            else:
                item = self.listWidget_2.item(4)
                item.setText(_translate("Dialog", ""))
            
            if("代达罗斯巢穴" in self.view5):
                item = self.listWidget_2.item(5)
                item.setText(_translate("Dialog", "代达罗斯巢穴"))
            else:
                item = self.listWidget_2.item(5)
                item.setText(_translate("Dialog", ""))

            if("火山巢穴" in self.view5):
                item = self.listWidget_2.item(6)
                item.setText(_translate("Dialog", "火山巢穴"))
            else:
                item = self.listWidget_2.item(6)
                item.setText(_translate("Dialog", ""))
            
            if("守卫者巢穴" in self.view5):
                item = self.listWidget_2.item(7)
                item.setText(_translate("Dialog", "守卫者巢穴"))
            else:
                item = self.listWidget_2.item(7)
                item.setText(_translate("Dialog", ""))
            
            if("台风金巢穴" in self.view5):
                item = self.listWidget_2.item(8)
                item.setText(_translate("Dialog", "台风金巢穴"))
            else:
                item = self.listWidget_2.item(8)
                item.setText(_translate("Dialog", ""))
            item = self.listWidget_2.item(9)
            item.setText(_translate("Dialog", ""))
            item = self.listWidget_2.item(10)
            item.setText(_translate("Dialog", ""))
            item = self.listWidget_2.item(11)
            item.setText(_translate("Dialog", ""))
            item = self.listWidget_2.item(12)
            item.setText(_translate("Dialog", ""))
            nxIndex=8
            if(len(newNxList)!=0):
                for index in range(len(newNxList)):
                    nxIndex=nxIndex+1
                    item = self.listWidget_2.item(nxIndex)
                    item.setText(_translate("Dialog", newNxList[index]))  
            self.listWidget_2.setSortingEnabled(__sortingEnabled)
        # except:
        #     print("查看失败")
    def showMaxTask(self,maxIndex,DWBH):
        try:
            maxTaskList = []
            connSelect= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
            curSelect = connSelect.cursor()
            maxIndex = maxIndex + 1
            for index in range(1,maxIndex):                
                sql = "SELECT DISTINCT JQBH,ZH,JSBH,RWMC,LCBH FROM taskdata WHERE DWBH = '"+DWBH+"' AND LCBH = '"+str(index)+"'"
                curSelect = connSelect.cursor()
                curSelect.execute(sql)
                viewList =curSelect.fetchall()
                if(len(maxTaskList)<1):
                    maxTaskList = viewList
                else:
                    if(len(maxTaskList)>len(viewList)):
                        maxTaskList = maxTaskList
                    else :
                        maxTaskList = viewList
            returnList = []
            returnList.append(maxTaskList)
            returnList.append(True)
            connSelect.close()
            return  returnList
        except:
            print("失败")  
    # 清除数据
    def removeVal(self):
        connDelete= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
        curDelete = connDelete.cursor()
        curDelete.execute(self.deleteSql)
        connDelete.commit()

        curDelete.execute(self.deleteUserSql)
        connDelete.commit()

        connDelete.close() 
        self.showTask()
    # 刷副本
    def switchUser(self):
       
        try:
            print(self.RMSL)
            switchSelSql = "SELECT PLZ FROM account WHERE ZH = '"+self.ZHVal+"' AND JSBH = '"+self.JSBHVal+"'"
            connSelect= pymysql.connect(host=hostVal, port=portVal, user=userVal, passwd=passwdVal, db=dbVal, charset='utf8')
            curSelect = connSelect.cursor()
            curSelect.execute(switchSelSql)
            val = curSelect.fetchall()
            if(int(val[0][0]) - int(self.RMSL)>0):
                PLZNum = int(val[0][0]) - int(self.RMSL)
                switchSql = "UPDATE account SET PLZ = "+str(PLZNum)+" WHERE ZH = '"+self.ZHVal+"' AND JSBH = '"+self.JSBHVal+"'"
                curSelect.execute(switchSql)
                connSelect.commit()
                connSelect.close()
            
            elif(int(val[0][0]) - int(self.RMSL)<0):
                PLZNum = 0
                switchSql = "UPDATE account SET PLZ = "+str(PLZNum)+" WHERE ZH = '"+self.ZHVal+"' AND JSBH = '"+self.JSBHVal+"'"
                curSelect.execute(switchSql)
                connSelect.commit()
                connSelect.close()
            self.getAccount("0")
        # if(val[0][0]=="A"):
        #     switchSql = "UPDATE account SET LCBH = 'B' WHERE ZH = '"+self.ZHVal+"' AND JSBH = '"+self.JSBHVal+"'"
        #     curSelect.execute(switchSql)
        #     connSelect.commit()
        #     connSelect.close()
        #     self.getAccount("0","1")
        # elif(val[0][0]=="B"):
        #     switchSql = "UPDATE account SET LCBH = 'A' WHERE ZH = '"+self.ZHVal+"' AND JSBH = '"+self.JSBHVal+"'"
        #     curSelect.execute(switchSql)
        #     connSelect.commit()
        #     connSelect.close()
        #     self.getAccountB("0")
        except:
           print("改变批次错误")
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
        self.getAccount("0")       
    def pageGet1(self):
        self.DJTVal = 1
        self.LCBHUserVal = "A"
        self.getAccount("0")
    def pageGet2(self):
        self.DJTVal = 2
        self.LCBHUserVal = "A"
        self.getAccount("0")
    def pageGet3(self):
        self.DJTVal = 3
        self.LCBHUserVal = "A"
        self.getAccount("0")
    def pageGet4(self):
        self.DJTVal = 4
        self.LCBHUserVal = "A"
        self.getAccount("0")
    def pageGet5(self):
        self.DJTVal = 1
        self.LCBHUserVal = "B"
        self.getAccount("0")
    def pageGet6(self):
        self.DJTVal = 2
        self.LCBHUserVal = "B"
        self.getAccount("0")
    def pageGet7(self):
        self.DJTVal = 3
        self.LCBHUserVal = "B"
        self.getAccount("0")
        # print("备注")
    def pageGet8(self):
        self.DJTVal = 4
        self.LCBHUserVal = "B"
        self.getAccount("0")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.getAccount("0")
        self.pushButton.setText(_translate("Dialog", "A1"))
        self.pushButton.clicked.connect(self.pageGet1)

        self.pushButton_2.setText(_translate("Dialog", "A2"))
        self.pushButton_2.clicked.connect(self.pageGet2)

        self.pushButton_3.setText(_translate("Dialog", "A3"))
        self.pushButton_3.clicked.connect(self.pageGet3)

        self.pushButton_4.setText(_translate("Dialog", "A4"))
        self.pushButton_4.clicked.connect(self.pageGet4)

        self.pushButton_5.setText(_translate("Dialog", "B1"))
        self.pushButton_5.clicked.connect(self.pageGet5)

        self.pushButton_11.setText(_translate("Dialog", "B2"))
        self.pushButton_11.clicked.connect(self.pageGet6)

        self.pushButton_12.setText(_translate("Dialog", "B3"))
        self.pushButton_12.clicked.connect(self.pageGet7)

        self.pushButton_13.setText(_translate("Dialog", "B4"))
        self.pushButton_13.clicked.connect(self.pageGet8)

        
        self.pushButton_6.setText(_translate("Dialog", "登录"))
        self.pushButton_6.clicked.connect(self.loginSelect)

        self.pushButton_7.setText(_translate("Dialog", "频道"))
        self.pushButton_7.clicked.connect(self.EnterClick)

        self.pushButton_14.setText(_translate("Dialog", "角色"))
        self.pushButton_14.clicked.connect(self.selectRole)

        self.pushButton_10.setText(_translate("Dialog", "截图"))
        self.pushButton_10.clicked.connect(self.startDelTask)

        self.pushButton_8.setText(_translate("Dialog", "截图2"))
        self.pushButton_8.clicked.connect(self.againDelTask)


        self.pushButton_15.setText(_translate("Dialog", "查看"))
        self.pushButton_15.clicked.connect(self.showTask)

        self.pushButton_16.setText(_translate("Dialog", "刷副本"))
        self.pushButton_16.clicked.connect(self.switchUser)

        self.pushButton_17.setText(_translate("Dialog", "清除"))
        self.pushButton_17.clicked.connect(self.removeVal)

        self.pushButton_19.setText(_translate("Dialog", "备用"))
        # self.pushButton_19.clicked.connect(self.inI)


        self.pushButton_9.setText(_translate("Dialog", "备用"))
        self.pushButton_18.setText(_translate("Dialog", "备用"))
        # self.pushButton_19.setText(_translate("Dialog", "备用"))
        self.pushButton_20.setText(_translate("Dialog", "备用"))

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())