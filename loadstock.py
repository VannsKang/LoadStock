import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        # self.kiwoom.OnEventConnect.connect(self.event_connect)
        # self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)

        self.setWindowTitle("Stockcode")
        self.setGeometry(300, 300, 300, 150)

        # label = QLabel('StockCode: ', self)
        # label.move(20, 20)

        # self.code_edit = QLineEdit(self)
        # self.code_edit.move(80, 20)
        # self.code_edit.setText("039490")

        btn1 = QPushButton("Get Stockcode", self)
        btn1.move(190, 10)
        btn1.clicked.connect(self.btn1_clicked)

        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(10, 10, 170, 130)

        # self.text_edit = QTextEdit(self)
        # self.text_edit.setGeometry(10,60,280,80)

        # self.text_edit.setEnabled(False)

        # btn1 = QPushButton("Login", self)
        # btn1.move(20,20)
        #
        # btn1 = QPushButton("Check state", self)
        # btn1.move(20, 70)
        # btn1.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        # code = self.code_edit.text()
        # self.text_edit.append("StockCode: "+code)
        #
        # self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "StockCode", code)
        #
        # self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10001_req", "opt10001", 0, "0101")

        # account_num = self.kiwoom.dynamicCall("GetLoginInfo(QString)", ["ACCNO"])
        # self.text_edit.append("Account Info: " + account_num.rstrip(';'))
        #
        ret = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", ["0"])
        kospi_code_list = ret.split(';')
        kospi_code_name_list = []

        for x in kospi_code_list:
            name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)", [x])
            kospi_code_name_list.append(x+" : "+name)

        self.listWidget.addItems(kospi_code_name_list)

    # def event_connect(self, err_code):
    #     if err_code == 0:
    #         self.text_edit.append("Login Success")

    # def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
    #     if rqname == "opt10001_req":
    #         name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "Stockname")
    #         volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "Stockvolume")
    #         self.text_edit.append("Stockname: " + name.strip())
    #         self.text_edit.append("Stockvolume: " + volume.strip())


    # def btn2_clicked(self):
    #     if self.kiwoom.dynamicCall("GetConnectState()") == 0 :
    #         self.statusBar().showMessage("Not connected")
    #     else:
    #         self.statusBar().showMessage("Connected")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()

# app = QApplication(sys.argv)
# print(sys.argv)
# label = QLabel("Hello PyQt")
# label.show()
# app.exec_()

# class Parent:
#     house = "yong-san"
#     def __init__(self):
#         self.money = 10000
#         pass
#
# class Child1(Parent):
#     def __init__(self):
#         super().__init__()
#         pass
#
# class Child2(Parent):
#     def __init__(self):
#         pass
#
# child1 = Child1()
# child2 = Child2()
#
# print('Child1', dir(child1))
# print('Child2', dir(child2))