#Finite field of order p class - maybe later can try work with finite fields of order p^n, need to define a 'quotient structure' 
import math

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
            raise ValueError 

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


    def totient(n):
        #There has to be a good way of doing this, don't know it yet. Maybe in terms of trees?
        #for now, implement only for primes:
        """ Returns the euler totient of n

        args

        n: int

        returns

        phi(n), where phi is the euler totient function. As this is the gp_element class, this is only defined in the case where n is a prime
        """
        if isprime(n) == True:
            return n-1

    def isprime(n):
        assert isinstance(n, int)
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    def is_generator(self, print_residues = False):
        """ Checks whether an element generates Z/pZ

            args

            self: ModP
            print_residues: Bool

            returns

            True if self is a generator, false if otherwise. Prints the list of residues mod p.
        """
        residues = [self.reduction]
        assert isinstance(print_residues, bool)
        
        if print_residues == False:
            for i in range(self.p):
                self *= self
                residues.append(self.reduction)
                if len(residues) != len(set(residues)):
                    return False
            return True

        if print_residues == True:
            for i in range(self.p):
                self *= self
                residues.append(self.reduction)
                if len(residues) != len(set(residues)):
                    return False
            print(residues)
            return True



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


    ModP(2,3).is_generator(print_residues = True)
