from fuzzylogic.fuzzyset import FuzzySet


class FuzzySystem:
    def __init__(self, entry_set: FuzzySet, out_set: FuzzySet, rules: list):
        """
        :param rules: list of rules
        :param entry_set: list of fuzzy sets which are entry sets
        :param out_set: list of fuzzy sets which are out sets
        """
        self.entry_fuzzy_set: FuzzySet = entry_set
        self.out_fuzzy_set: FuzzySet = out_set
        self.rules: list = rules

    def resolve_rules(self, fuzzy_value: dict):
        """
        :param fuzzy_value: created by fuzzification done on entry_fuzzy_set
        :return:
        """
        result_fuzzy_value: dict = {}
        for rule in self.rules:
            result_fuzzy_value[rule.affected] = fuzzy_value.get(rule.parent)
        return result_fuzzy_value

    def compute(self, entry: float):
        """
        :param entry: "user" input value to solve by fuzzy system
        :return: value calculated by fuzzy system
        """
        fuzzy_value = self.entry_fuzzy_set.fuzzificate_value(entry)
        fuzzy_value_transformed = self.resolve_rules(fuzzy_value)
        result_term = self.out_fuzzy_set.conclude(fuzzy_value_transformed)

        divided = 0
        divider = 0
        for x, value in zip(self.out_fuzzy_set.value_axes[0], result_term):
            divided += x * value
            divider += value
        if divider == 0:
            return 0
        else:
            return divided / divider
