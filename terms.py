class Term:
    def __init__(self, begin: float, end: float, name: str):
        self.name: str = name
        self.begin: float = begin
        self.end: float = end
        self.values: list = []

    def build(self, x_axis: list):
        pass


class TriangleTerm(Term):
    def __init__(self, x1: float, begin: float, end: float, name: str):
        super().__init__(begin, end, name)
        self.x1 = x1

    def build(self, x_axis: list):
        for x in x_axis:
            if self.begin <= x <= self.x1:
                value = (x - self.begin) / (self.x1 - self.begin)
                self.values.append(value)
            elif self.x1 <= x <= self.end:
                value = (self.end - x) / (self.end - self.x1)
                self.values.append(value)
            else:
                self.values.append(0)


class SquareTerm(Term):
    def __init__(self, x1: float, x2: float, begin: float, end: float, name: str):
        super().__init__(begin, end, name)
        self.x1 = x1
        self.x2 = x2

    def build(self, x_axis: list):
        for x in x_axis:
            if self.begin <= x <= self.x1:
                value = (x - self.begin) / (self.x1 - self.begin)
                self.values.append(value)
            elif self.x1 <= x <= self.x2:
                self.values.append(1)
            elif self.x2 <= x <= self.end:
                value = (self.end - x) / (self.end - self.x2)
                self.values.append(value)
            else:
                self.values.append(0)
