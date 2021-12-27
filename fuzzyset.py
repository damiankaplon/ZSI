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
            x_axis_values.append(x_axis_values[i] + self.step_value)
        self.value_axes[0] = x_axis_values

    def build_terms(self):
        self.erase_terms()
        for term in self.terms:
            self.__build_term(term)

    def __build_term(self, term: Term):
        term.build(self.value_axes[0])
        self.value_axes.append(term.values)

    def erase_terms(self):
        for i in range(0, len(self.value_axes) - 1):
            if i == 0:
                pass
            else:
                self.value_axes.remove(i)

    def fuzz_the_input(self, input: float) -> dict:
        fuzzy_result = dict()
        index = self.value_axes[0].index(input)
        for term in self.terms:
            fuzzy_result[term.name] = term.values[index]
        return fuzzy_result
