from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

from fuzzylogic.fuzzysystem import FuzzySystem
from time import sleep


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, fuzzy_system):
        self.fuzzy_system = fuzzy_system

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(428, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_temp = QtWidgets.QSlider(self.centralwidget)
        self.user_temp.setGeometry(QtCore.QRect(40, 9, 20, 221))
        self.user_temp.setMaximum(9000)
        self.user_temp.setSingleStep(1)
        self.user_temp.setOrientation(QtCore.Qt.Vertical)
        self.user_temp.setObjectName("user_temp")
        self.actual_temp = QtWidgets.QSlider(self.centralwidget)
        self.actual_temp.setGeometry(QtCore.QRect(40, 240, 21, 291))
        self.actual_temp.setMaximum(10000)
        self.actual_temp.setOrientation(QtCore.Qt.Vertical)
        self.actual_temp.setObjectName("actual_temp")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 71, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 240, 101, 17))
        self.label_2.setObjectName("label_2")
        self.lcd_fuzzy_output = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_fuzzy_output.setGeometry(QtCore.QRect(240, 40, 151, 61))
        self.lcd_fuzzy_output.setObjectName("lcd_fuzzy_output")
        self.lcd_user_temp = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_user_temp.setGeometry(QtCore.QRect(60, 30, 71, 31))
        self.lcd_user_temp.setFrameShape(QtWidgets.QFrame.Box)
        self.lcd_user_temp.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcd_user_temp.setLineWidth(1)
        self.lcd_user_temp.setObjectName("lcd_user_temp")
        self.lcd_actual_temp = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_actual_temp.setGeometry(QtCore.QRect(60, 260, 71, 31))
        self.lcd_actual_temp.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcd_actual_temp.setObjectName("lcd_actual_temp")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 20, 41, 21))
        self.label_3.setObjectName("label_3")
        self.simulate_button = QtWidgets.QPushButton(self.centralwidget)
        self.simulate_button.setGeometry(QtCore.QRect(300, 110, 89, 25))
        self.simulate_button.setObjectName("simulate_button")
        self.winter_button = QtWidgets.QPushButton(self.centralwidget)
        self.winter_button.setGeometry(QtCore.QRect(260, 240, 61, 25))
        self.winter_button.setObjectName("winter_button")
        self.summer_button = QtWidgets.QPushButton(self.centralwidget)
        self.summer_button.setGeometry(QtCore.QRect(330, 240, 61, 25))
        self.summer_button.setObjectName("summer_button")
        self.put_out_button = QtWidgets.QPushButton(self.centralwidget)
        self.put_out_button.setGeometry(QtCore.QRect(260, 270, 131, 25))
        self.put_out_button.setObjectName("put_out_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.user_temp.valueChanged.connect(self.value_changed)
        self.actual_temp.valueChanged.connect(self.value_changed)
        self.winter_button.clicked.connect(self.set_winter)
        self.summer_button.clicked.connect(self.set_summer)
        self.put_out_button.clicked.connect(self.put_out_fire)
        self.simulate_button.clicked.connect(self.simulate)
        self.timer = QTimer()
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.increment_actual_temp)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "User temp"))
        self.label_2.setText(_translate("MainWindow", "Actual temp"))
        self.label_3.setText(_translate("MainWindow", "Angel"))
        self.simulate_button.setText(_translate("MainWindow", "Simulate"))
        self.winter_button.setText(_translate("MainWindow", "Winter"))
        self.summer_button.setText(_translate("MainWindow", "Summer"))
        self.put_out_button.setText(_translate("MainWindow", "Put out"))

    def value_changed(self):
        actual_temp = round(self.actual_temp.value() / 100, 1)
        user_temp = round(self.user_temp.value() / 100, 1)
        result = self.fuzzy_system.compute(calc_input_for_fuzzy_system(actual_temp, user_temp))
        self.lcd_user_temp.display(user_temp)
        self.lcd_actual_temp.display(actual_temp)
        self.lcd_fuzzy_output.display(result)

    def set_winter(self):
        self.user_temp.setValue(8000)

    def set_summer(self):
        self.user_temp.setValue(6000)

    def put_out_fire(self):
        self.user_temp.setValue(0)

    def simulate(self):
        actual_temp = round(self.actual_temp.value() / 100, 1)
        user_temp = round(self.user_temp.value() / 100, 1)
        if actual_temp <= user_temp:
            self.timer.start()

    def increment_actual_temp(self):
        actual_temp = round(self.actual_temp.value() / 100, 1)
        user_temp = round(self.user_temp.value() / 100, 1)
        if actual_temp >= user_temp:
            self.timer.stop()
        else:
            temp_to_set = self.actual_temp.value() + 10
            self.actual_temp.setValue(temp_to_set)


def calc_input_for_fuzzy_system(actual_temp: float, user_temp: float):
    return round(actual_temp - user_temp, 1)
