from excpetions import InputError
from terms import Term


class FuzzySet:
    def __init__(self, begin_value: int, end_value: int, step_value: float, terms: list):
        self.begin_value: int = begin_value
        self.end_value: int = end_value
        self.step_value: float = step_value
        self.x_axis_length: int = self.__calc_x_axis_length()
        self.value_axes: list = [[self.begin_value, ], ]
        self.__set_x_axis_values()
        self.terms: list = terms
        self.build_terms()

    def __calc_x_axis_length(self) -> int:
        return round(abs(self.end_value - self.begin_value) / self.step_value)

    def __set_x_axis_values(self):
        x_axis_values: list = [self.begin_value, ]
        for i in range(0, self.x_axis_length):
            x_axis_values.append(round((x_axis_values[i] + self.step_value), 2))
        self.value_axes[0] = x_axis_values

    def build_terms(self):
        self.erase_terms()
        for term in self.terms:
            self.__build_term(term)

    def __build_term(self, term: Term):
        term.build(self.value_axes[0])
        self.value_axes.append(term.values)

    def erase_terms(self):
        for i in range(len(self.value_axes) - 1, 0, -1):
            self.value_axes.pop(i)

    def fuzzificate_value(self, entry: float) -> dict:
        """
        :param entry:
        :return: fuzzy_value: dict key - name of term, value - the value of belonging
        """
        fuzzy_result = dict()
        index = self.value_axes[0].index(entry)
        for term in self.terms:
            fuzzy_result[term.name] = term.values[index]
        return fuzzy_result

    def conclude(self, fuzzy_entry: dict):
        """
        :param fuzzy_entry:  dict key - name of term, value - the value of belonging
        :return:
        """
        # validating input
        if len(fuzzy_entry) != len(self.terms):
            raise InputError("Fuzzy value doesnt match amount of terms")
        for term in self.terms:
            if term.name not in fuzzy_entry.keys():
                raise InputError("Fuzzy value keys doesnt match one/some of the names of terms")
        # stop
        i = 1
        for term in self.terms:
            cut_value = fuzzy_entry.get(term.name)
            self.value_axes[i] = term.cut(cut_value)
            i += 1

        result = []
        for i in range(len(self.value_axes[0])):
            maximum = 0
            for j in range(1, len(self.value_axes)):
                maximum = max(maximum, self.value_axes[j][i])
                if j == len(self.value_axes) - 1:
                    result.append(maximum)

        self.build_terms()
        return result
