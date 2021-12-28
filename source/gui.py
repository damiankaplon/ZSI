from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_temp = QtWidgets.QSlider(self.centralwidget)
        self.user_temp.setGeometry(QtCore.QRect(40, 50, 16, 160))
        self.user_temp.setOrientation(QtCore.Qt.Vertical)
        self.user_temp.setObjectName("user_temp")
        self.actual_temp = QtWidgets.QSlider(self.centralwidget)
        self.actual_temp.setGeometry(QtCore.QRect(40, 220, 16, 160))
        self.actual_temp.setOrientation(QtCore.Qt.Vertical)
        self.actual_temp.setObjectName("actual_temp")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 71, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 220, 101, 17))
        self.label_2.setObjectName("label_2")
        self.fuzzy_output = QtWidgets.QLCDNumber(self.centralwidget)
        self.fuzzy_output.setGeometry(QtCore.QRect(550, 170, 151, 61))
        self.fuzzy_output.setObjectName("fuzzy_output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "User temp"))
        self.label_2.setText(_translate("MainWindow", "Actual temp"))