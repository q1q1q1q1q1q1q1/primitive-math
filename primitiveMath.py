

class unsigned:
    def __init__(self, value: [int, float]):
        self.value = value
        assert (self.value > 0 and "the value cannot be less than or equal to zero")

    def __str__(self):
        return "Unsigned " + (type(self.value))

class primitiveMath:
    """Newton’s method"""
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

    def least_common_divisor(self, a: [int, float], b: [int, float]) -> [int, float]:
        """Euclid’s Algorithm"""
        """bk+1 ≥ bk + bk−1 ≥ Fib(k) + Fib(k − 1) = Fib(k + 1)"""
        '''
        EA:
        mov eax, ebx
        div ecx, ebx
        mov ebx, edx
        jmp main 
        
        main:
        mov ecx, a
        mov ebx, b
        cmp ebx, 0
        jne EA       
        
        '''
        while b != 0:
            #copy last result from a%b
            temp: [float, int] = b
            b = a % b
            a = temp
        return a
