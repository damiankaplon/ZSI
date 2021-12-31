from PyQt5 import QtCore, QtGui, QtWidgets

from fuzzylogic.fuzzysystem import FuzzySystem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, fuzzy_system):
        self.fuzzy_system = fuzzy_system
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 453)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_temp = QtWidgets.QSlider(self.centralwidget)
        self.user_temp.setGeometry(QtCore.QRect(40, 50, 16, 160))
        self.user_temp.setMaximum(9000)
        self.user_temp.setSingleStep(1)
        self.user_temp.setOrientation(QtCore.Qt.Vertical)
        self.user_temp.setObjectName("user_temp")
        self.actual_temp = QtWidgets.QSlider(self.centralwidget)
        self.actual_temp.setGeometry(QtCore.QRect(40, 220, 16, 160))
        self.actual_temp.setMaximum(10000)
        self.actual_temp.setOrientation(QtCore.Qt.Vertical)
        self.actual_temp.setObjectName("actual_temp")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 71, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 220, 101, 17))
        self.label_2.setObjectName("label_2")
        self.lcd_fuzzy_output = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_fuzzy_output.setGeometry(QtCore.QRect(340, 150, 151, 61))
        self.lcd_fuzzy_output.setObjectName("lcd_fuzzy_output")
        self.lcd_user_temp = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_user_temp.setGeometry(QtCore.QRect(60, 70, 64, 23))
        self.lcd_user_temp.setObjectName("lcd_user_temp")
        self.lcd_actual_temp = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_actual_temp.setGeometry(QtCore.QRect(60, 240, 64, 23))
        self.lcd_actual_temp.setObjectName("lcd_actual_temp")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 130, 81, 21))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.user_temp.valueChanged.connect(self.value_changed)
        self.actual_temp.valueChanged.connect(self.value_changed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "User temp"))
        self.label_2.setText(_translate("MainWindow", "Actual temp"))
        self.label_3.setText(_translate("MainWindow", "Angel"))

    def value_changed(self):
        actual_temp = round(self.actual_temp.value() / 100, 1)
        user_temp = round(self.user_temp.value() / 100, 1)
        result = self.fuzzy_system.compute(calc_input_for_fuzzy_system(actual_temp, user_temp))
        self.lcd_user_temp.display(user_temp)
        self.lcd_actual_temp.display(actual_temp)
        self.lcd_fuzzy_output.display(result)


def calc_input_for_fuzzy_system(actual_temp: float, user_temp: float):
    return round(actual_temp - user_temp, 1)
