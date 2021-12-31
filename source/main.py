#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets
from fuzzylogic.fuzzyset import FuzzySet
from fuzzylogic.fuzzysystem import FuzzySystem
from fuzzylogic.rule import Rule
from fuzzylogic.terms import TriangleTerm, SquareTerm
from gui import Ui_MainWindow


def create_fuzzy_system() -> FuzzySystem:
    term_super_cold = SquareTerm(-10, -8, -10, -6.75, "super cold")
    term_very_cold = SquareTerm(-7, -5.5, -7.5, -5, "very cold")
    term_cold = SquareTerm(-5.25, -3.5, -6.5, -3, "cold")
    term_almost_cold = SquareTerm(-3, -2, -3.5, -1.5, "almost cold")
    term_chill = TriangleTerm(-1, -2, 0, "chill")
    entry_terms = [term_super_cold, term_very_cold, term_cold, term_almost_cold, term_chill]
    fuzzy_entry_set = FuzzySet(-10, 0, 0.1, entry_terms)
    term_very_small = TriangleTerm(10, 0, 20, "very small")
    term_small = TriangleTerm(20, 10, 30, "small")
    term_medium = TriangleTerm(45, 20, 60, "medium")
    term_big = TriangleTerm(60, 45, 80, "big")
    term_very_big = TriangleTerm(80, 60, 90, "very big")
    out_terms = [term_very_small, term_small, term_medium, term_big, term_very_big]
    fuzzy_out_set = FuzzySet(0, 90, 0.5, out_terms)
    rules = [Rule("super cold", "very big"), Rule("very cold", "big"), Rule("cold", "medium"),
             Rule("almost cold", "small"), Rule("chill", "very small")]
    return FuzzySystem(fuzzy_entry_set, fuzzy_out_set, rules)


def set_up_gui():
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window, create_fuzzy_system())
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #create_fuzzy_system()
    set_up_gui()
