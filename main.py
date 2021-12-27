#!/usr/bin/env python3

# TODO zrobimy tu pewnie jakies proste gui z Tkinter
from fuzzyset import FuzzySet
from terms import TriangleTerm, SquareTerm


def main():
    term_super_cold = SquareTerm(-10, -8, -10, -6.75, "super cold")
    term_very_cold = SquareTerm(-7, -5.5, -7.5, -5, "very cold")
    term_cold = SquareTerm(-5.25, -3.5, -6.5, -3, "cold")
    term_almost_cold = SquareTerm(-3, -2, -3.5, -1.5, "almost cold")
    term_chill = TriangleTerm(-1, -2, 0, "chill")
    term_good = TriangleTerm(0, -0.25, 0, "good")
    term_list = [term_super_cold, term_very_cold, term_cold, term_almost_cold, term_chill, term_good]
    fuzzy_set = FuzzySet(-10, 0, 0.1, term_list)
    # print(fuzzy_set.fuzz_the_input(-7.3))


if __name__ == "__main__":
    main()
