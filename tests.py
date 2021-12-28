#!/usr/bin/env python3

import unittest
from unittest import TestCase

from fuzzyset import FuzzySet
from terms import *


class FuzzySetTest(TestCase):

    def test_x_axes_values(self):
        # GIVEN
        correct_list = [-10, -9.75, -9.5, -9.25, -9]
        # WHEN
        fuzzy_set = FuzzySet(-10, -9, 0.25, list())
        # THEN
        self.assertEqual(correct_list, fuzzy_set.value_axes[0])

    def test_fuzzification(self):
        # GIVEN
        term = SquareTerm(-7, -5.5, -7.5, -5, "Very cold")
        term2 = SquareTerm(-5.25, -3.5, -6, -3, "cold")
        term_list = [term, term2]
        fuzzy_set = FuzzySet(-10, 0, 0.1, term_list)
        # WHEN
        result = fuzzy_set.fuzzificate_value(-5.5)
        # THEN
        self.assertDictEqual({'Very cold': 1, 'cold': 0.667}, result)

    def test_conclude(self):
        # GIVEN
        term = SquareTerm(-7, -5.5, -7.5, -5, "Very cold")
        term2 = SquareTerm(-5.25, -3.5, -6, -3, "cold")
        term_list = [term, term2]
        fuzzy_set = FuzzySet(-10, 0, 0.1, term_list)
        # WHEN
        fuzzy_value: dict = {"Very cold": 0.5, "cold": 0.3}
        result = fuzzy_set.conclude(fuzzy_value)
        # THEN
        self.assertTrue(max(result) < max(fuzzy_set.value_axes[1]))
        self.assertTrue(max(result) == 0.5)
        self.assertTrue(len(fuzzy_set.value_axes[0]) == len(result))


class TermsTest(TestCase):

    def test_build_term(self):
        # GIVEN
        x_axis: list = [-10, -9.75, -9.5, -9.25, -9, -8.75, -8.5, -8.25, -8, -7.75, -7.5, -7.25, -7, -6.75, -6.5, -6.25]
        term: TriangleTerm = TriangleTerm(-9, -10, -8, "term name")
        # WHEN
        term.build(x_axis)
        # THEN
        expected_term_values: list = [0.0, 0.25, 0.5, 0.75, 1.0, 0.75, 0.5, 0.25, 0.0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected_term_values, term.values)

    def test_eq(self):
        term1 = Term(1, 2, "name")
        term2 = Term(2, 3, "other name")
        self.assertTrue(term1 != term2)

    def test_cut(self):
        # GIVEN
        term = SquareTerm(-8.75, -8, -9.75, -6.25, "Very cold")
        x_axis: list = [-10, -9.75, -9.5, -9.25, -9, -8.75, -8.5, -8.25, -8, -7.75, -7.5, -7.25, -7, -6.75, -6.5, -6.25]
        term.build(x_axis)
        # WHEN
        cut_values = term.cut(0.5)
        # THEN
        expected_values = [0, 0, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.429, 0.286, 0.143, 0.0]
        self.assertEqual(expected_values, cut_values)


if "__main__" == __name__:
    unittest.main()
