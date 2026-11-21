class fraction:
    def __init__(self ,numerator, denominator):
        self.n = numerator
        self.d = denominator
        def _add_(self, other):
            return fraction(self.n * other.d + self.d * other.n, self.d * other.d)
        def __str__(self):
            return f"{self.n}/{self.d}"
f1 = fraction(1, 2)
f2 = fraction(1, 3)

print(f1 + f2)