#Finite field of order p class - maybe later can try work with finite fields of order p^n, need to define a 'quotient structure' 

class ModP:
    def __init__(self, a, p)-> None:
        self.reduction = a % p
        self.p = p

    #equality     
    def __eq__(self,other):
        if isinstance(other, ModP):
            return self == other
        else:
            return NotImplemented

    #addition of two integers modulo p
    def __add__(self,other):
        if isinstance(other, ModP) and self.p == other.p:
            return(ModP(self.reduction + other.reduction, self.p))
        else:
            return NotImplemented
    
    #addition of an integer modulo p with an integer

    def __radd__(self, other):
        assert isinstance(other,int)
        return ModP(self.reduction + other, self.p)
     
    '''
    quick note on __radd__. When we do ModP(7,13) + 4, python inteprets that as ModP(7,13).__add__(4). If that __add__ method is not implemented,
    it will run ModP(7,13).__radd__(4). We can do a similar thing for multiplication, where one of the multiplications is multiplying two instances of 
    the class ModP, and another is multiplying a ModP object with an integer.

    '''                   
    #negation method
     
    def __neg__(self):
        return(ModP(-1*self.reduction, self.p))
    
    #subtraction method
    def __sub__(self,other):
        return self +  -other
     
    #multiplication method

    def __mul__(self,other):    
        if isinstance(other, ModP) and other.p == self.p:
            return ModP(self.reduction * other.reduction, self.p)
        else:
            NotImplemented

    def __rmul__(self,other):
        assert isinstance(other, int)
        return ModP(self.reduction * other, self.p)

    #static extended euclidean algorithm
    @staticmethod
    def extgcd(a,b):
        #returns gcd, x ,y in ax+by = gcd
        if b == 0:
            return a, 1, 0 
        g, x1, y1 = ModP.extgcd(b, a%b)
        x = y1
        y = x1 - a//b * y1 
        return g, x, y

    #finding inverse method
    def inv(self):
        if self.reduction != 0:
            return ModP(ModP.extgcd(self.reduction, self.p)[1], self.p)
        else:
            return NotImplemented


    #division method
    def __truediv__(self, other): 
        if isinstance(other, ModP) and self.p == other.p:
            return ModP((self.inv() * other).reduction, self.p)
        else:
            return NotImplemented


    #string method
    def __str__(self):
        return '%s mod %s' % (self.reduction, self.p)
   

    #print representative method
    def __repr__(self):
        return '%s(%s, %s)' % (self.__class__.__name__, self.reduction, self.p)

    # solves a system of congruences 
    def crt(self, other):
        pass

    #returns a generator mod p
    #Very inefficient: be warned
    def get_generator(p: int) -> ModP:
        pass


if __name__ == '__main__':
    #here is the place to test everything
    print(ModP.extgcd(7,3))
    test1 = ModP(10,17)
    test2 = ModP(12,17)
    t3 = test2.inv()
    test3 = ModP(0,19)
    '''
    print(repr(t3))
    print(repr(test2.inv() * test2))
    print(repr(test1.div(test2)))
    '''
    print(repr(test1 / test2))

    print(test2.div(test3))
