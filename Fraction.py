class Fraction:
    def __init__(self, a: int, b: int):
        d = Fraction.gcd(a,b)
        self.a = a / d
        self.b = b / d
    
    def gcd(a,b):
        if b == 0:
            return a
        while b:
            Fraction.gcd(b, a%b)
    

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self == other
        else:
            return False
        
    def __add__(self, other):
        return Fraction(self.a * other.b + self.b * other.a, self.b *other.b) 
    
    def __radd__(self, other):
        assert isinstance(other, int)
        return Fraction(self.a + self.b*other, self.b)
    
    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)  

    def __rmul__(self, other):
        pass

    def __inv__(self):
        return Fraction(self.b, self.a)

    def __truediv__(self, other):
        return self.inv() * other

    def __str__(self):
        return '%s/%s' % (self.a, self.b)

    def __repr__(self):
        pass

if __name__ == '__main__':
   pass