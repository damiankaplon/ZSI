from fuzzylogic.excpetions import InputError


class FuzzySystem:
    def __init__(self, entry_sets: list, out_sets: list):
        """
        :param entry_sets: list of fuzzy sets which are entry sets
        :param out_sets: list of fuzzy sets which are out sets
        """
        self.entry_fuzzy_sets: list = entry_sets
        self.out_fuzzy_sets: list = out_sets

    def compute(self, entries: list):
        """
        :param entries: list of "user" input values to solve by fuzzy system. Quantity equal to amount of entry sets
        :return: value calculated by fuzzy system
        """
        if len(entries) != len(self.entry_fuzzy_sets):
            raise InputError("Entry amount has to be equal to amount of fuzzy system entry sets")

        fuzzificated_values: list = []
        i = 0
        for entry in entries:
            fuzzificated_values.append(self.entry_fuzzy_sets[i].fuzzificate_value(entry))
            i += 1


