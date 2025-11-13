class Complex:
    def __init__(self, re: float, im: float):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)        
    
    def __radd__(self, other):
        pass

    def __mul__(self, other):
        real_part = self.re * other.re - self.im * other.im
        im_part = self.re * other.im + self.im * other.re
        return Complex(real_part, im_part)

    def __rmul__(self, other):
        pass

    def __neg__(self):
        return Complex(-self.re, -self.im)

    def __sub__(self, other):
        return self.__add__(Complex.neg(other))

    def conjugate(self):
        return Complex(self.re, -self.im)
    
    @staticmethod
    def abs(self):
        pass

    def inv(self):
        pass

    def __truediv__(self, other):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

if __name__ == '__main__':
    pass
