# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TicTacToeUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Tic-Tac-Toe (MinMax)")
        MainWindow.resize(400, 431)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.B00 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.B00.sizePolicy().hasHeightForWidth())
        self.B00.setSizePolicy(sizePolicy)
        self.B00.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.B00.setFont(font)
        self.B00.setObjectName("B00")
        self.gridLayout.addWidget(self.B00, 0, 0, 1, 1)
        self.B10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.B10.sizePolicy().hasHeightForWidth())
        self.B10.setSizePolicy(sizePolicy)
        self.B10.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.B10.setFont(font)
        self.B10.setObjectName("B10")
        self.gridLayout.addWidget(self.B10, 1, 0, 1, 1)
        self.B11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.B11.sizePolicy().hasHeightForWidth())
        self.B11.setSizePolicy(sizePolicy)
        self.B11.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.B11.setFont(font)
        self.B11.setObjectName("B11")
        self.gridLayout.addWidget(self.B11, 1, 1, 1, 1)
        self.B12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.B12.sizePolicy().hasHeightForWidth())
        self.B12.setSizePolicy(sizePolicy)
        self.B12.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.B12.setFont(font)
        self.B12.setObjectName("B12")
        self.gridLayout.addWidget(self.B12, 1, 2, 1, 1)
        self.B22 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.B22.sizePolicy().hasHeightForWidth())
        self.B22.setSizePolicy(sizePolicy)
        self.B22.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.B22.setFont(font)
        self.B22.setStyleSheet("")
        self.B22.setObjectName("B22")
        self.gridLayout.addWidget(self.B22, 2, 2, 1, 1)
        self.B21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.B21.sizePolicy().hasHeightForWidth())
        self.B21.setSizePolicy(sizePolicy)
        self.B21.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.B21.setFont(font)
        self.B21.setObjectName("B21")
        self.gridLayout.addWidget(self.B21, 2, 1, 1, 1)
        self.B20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.B20.sizePolicy().hasHeightForWidth())
        self.B20.setSizePolicy(sizePolicy)
        self.B20.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.B20.setFont(font)
        self.B20.setObjectName("B20")
        self.gridLayout.addWidget(self.B20, 2, 0, 1, 1)
        self.B02 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.B02.sizePolicy().hasHeightForWidth())
        self.B02.setSizePolicy(sizePolicy)
        self.B02.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.B02.setFont(font)
        self.B02.setObjectName("B02")
        self.gridLayout.addWidget(self.B02, 0, 2, 1, 1)
        self.B01 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.B01.sizePolicy().hasHeightForWidth())
        self.B01.setSizePolicy(sizePolicy)
        self.B01.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.B01.setFont(font)
        self.B01.setObjectName("B01")
        self.gridLayout.addWidget(self.B01, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 350, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.B00.clicked.connect(lambda:self.Ac((0,0),self.B00))
        self.B01.clicked.connect(lambda:self.Ac((0,1),self.B01))
        self.B02.clicked.connect(lambda:self.Ac((0,2),self.B02))

        self.B10.clicked.connect(lambda:self.Ac((1,0),self.B10))
        self.B11.clicked.connect(lambda:self.Ac((1,1),self.B11))
        self.B12.clicked.connect(lambda:self.Ac((1,2),self.B12))

        self.B20.clicked.connect(lambda:self.Ac((2,0),self.B20))
        self.B21.clicked.connect(lambda:self.Ac((2,1),self.B21))
        self.B22.clicked.connect(lambda:self.Ac((2,2),self.B22))

        self.count=False
        self.row=0
        self.col=0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Tic-Tac-Toe (MinMax)", "Tic-Tac-Toe (MinMax)"))
        self.B00.setText(_translate("MainWindow", " "))
        self.B10.setText(_translate("MainWindow", " "))
        self.B11.setText(_translate("MainWindow", " "))
        self.B12.setText(_translate("MainWindow", " "))
        self.B22.setText(_translate("MainWindow", " "))
        self.B21.setText(_translate("MainWindow", " "))
        self.B20.setText(_translate("MainWindow", " "))
        self.B02.setText(_translate("MainWindow", " "))
        self.B01.setText(_translate("MainWindow", " "))
        self.label.setText(_translate("MainWindow", " "))
    
    def Ac(self,Val,B):
            B.setText("X")
            self.label.setText("Lets Go!")
            self.row=Val[0]
            self.col=Val[1]
            self.count=True
       





# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
