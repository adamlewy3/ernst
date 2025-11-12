class Fraction:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    
    def __eq__(self, other):
        if self.a * other.b == self.b * other.a:
            return True
        else:
            return False
        
    def __add__(self, other):
        return(Fraction(self.a * other.b + self.b * other.a, self.b *other.b))
    
    def __radd__(self, other):
        pass
    
    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __inv__(self, other):
        pass

    def div(self, other):
        pass

if __name__ == '__main__':
    pass