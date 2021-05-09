
def sqrt_make(value: [int, float]) -> [int, float]:
    approximation: [int, float] = 1
    accuracy_level: int = 0
    while accuracy_level < 50:
        coefficient: [int, float] = value / approximation
        approximation: [int, float] = (coefficient + approximation) / 2
        accuracy_level += 1
    return approximation

