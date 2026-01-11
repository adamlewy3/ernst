import math
class Fraction:
    def __init__(self, a: int, b: int):
        d = math.gcd(a,b)
        self.a = int(a / d)
        self.b = int(b / d)
    
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

    @classmethod
    def harmonic(cls, i: int):
        """Returns the i'th harmonic number:
            
        args:

        int: if 
            
        returns:

        Frac: i'th harmonic number

        """
        if i <= 0:
            raise ValueError("Input must be positive!")
        if i == 1:
            return cls(1,1)
        if i > 1:
            return cls(1,i) + Fraction.harmonic(i-1)  



if __name__ == '__main__':
    print("Hello, World!")
    
    test1 = Fraction(1,2)
    test2 = Fraction(1,3)
    print(test1)

    print(test1 +test2 + Fraction(1,1))

    print(Fraction.harmonic(3))
