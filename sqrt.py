


class unsigned:
    def __init__(self, value: [int, float]):
        self.value = value
        assert (self.value > 0 and "the value cannot be less than or equal to zero")


class primitiveMath:
    def sqrt_make(self, value: [int, float]) -> [int, float]:
        approximation: [int, float] = 1
        accuracy_level: int = 0
        while accuracy_level < 50:
            coefficient: [int, float] = value / approximation
            approximation: [int, float] = (coefficient + approximation) / 2
            accuracy_level += 1
        return approximation

    def exponentiation_of_two(self, value: [int, float], n: unsigned) -> unsigned:
        """b*b*b*b*b*b*b*b replace b^8 = b^4*b^4 and so on (degree of two)"""
        lvl: int = 2
        while lvl < n.value:
            value = value * value
            lvl += 2
        return value

