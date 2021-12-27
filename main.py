#!/usr/bin/env python3

# TODO zrobimy tu pewnie jakies proste gui z Tkinter
from fuzzyset import FuzzySet
from terms import TriangleTerm, SquareTerm


def main():
    term = SquareTerm(-7, -5.5, -7.5, -5, "Very cold")
    term2 = SquareTerm(-5.25, -3.5, -6, -3, "cold")
    term_list = [term, term2]
    fuzzy_set = FuzzySet(-10, 0, 0.25, term_list)
    print(fuzzy_set.fuzz_the_input(-5.5))


if __name__ == "__main__":
    main()
