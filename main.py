#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets
# TODO zrobimy tu pewnie jakies proste gui z Tkinter
from fuzzyset import FuzzySet
from terms import TriangleTerm, SquareTerm
from gui import Ui_MainWindow


def main():
    term_super_cold = SquareTerm(-10, -8, -10, -6.75, "super cold")
    term_very_cold = SquareTerm(-7, -5.5, -7.5, -5, "very cold")
    term_cold = SquareTerm(-5.25, -3.5, -6.5, -3, "cold")
    term_almost_cold = SquareTerm(-3, -2, -3.5, -1.5, "almost cold")
    term_chill = TriangleTerm(-1, -2, 0, "chill")
    term_good = TriangleTerm(0, -0.25, 0, "good")
    term_list = [term_super_cold, term_very_cold, term_cold, term_almost_cold, term_chill, term_good]
    fuzzy_input_set = FuzzySet(-10, 0, 0.1, term_list)
    print(fuzzy_input_set.fuzz_the_input(-7.3))


def set_up_gui():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    set_up_gui()
