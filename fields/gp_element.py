#Finite field of order p class - maybe later can try work with finite fields of order p^n, need to define a 'quotient structure' 
import math
import copy

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

    def pow(self, n):
        """ Fast Exponentiation method. 

        args

        self: ModP
        n: int

        returns

        self^n: ModP

        """
        power = n % ((self.p)-1)
        if power == 0:
            return ModP(1, self.p)
        else:
            partial = ModP.pow(self, power //2)
            result = partial*partial
            if power % 2 == 1:
                result *= self
            return result

    # solves a system of congruences 
    def crt(data):
        """ Returns the solution to the system

        x = self.reduction (self.p)
        x = other1.reduction (other1.p)
        x = other2.reduction (other2.p)

        args 

        data: list of ModP such that all are coprime.
        returns

        x: ModP
        """
        for i in range(len(data)):
            assert isinstance(data[i], ModP)

        for i in range(len(data)):
            for j in range(len(data)):
                if i != j and data[i].p == data[j].p:
                    raise ValueError("Must be pairwise coprime!")
        #Maybe better to do this with multiple i/o
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

    def residue_printer(self, data):
        for i in range(1,self.p):
            print(f"{self.reduction}^{i} = {data[i-1]}")

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
        self_copy = copy.deepcopy(self)
        
        if print_residues == False:
            for i in range(2,self.p):
                self *= self_copy
                residues.append(self.reduction)
                if len(residues) != len(set(residues)):
                    return False
            return True

        if print_residues == True:
            for i in range(2,self.p):
                self *= self_copy 
                residues.append(self.reduction)
                if len(residues) != len(set(residues)):
                    return False 
            self_copy.residue_printer(residues)
            return True
    
    def legendre(self):
        """
        Evaluates the legendre symbol (a/p), a is self

        args:
        a: int
        p: int

        returns:
        (a/p) mod p
        """
        res = self.pow(int((self.p-1)/2))
        if res.reduction == 1:
            return True
        else: 
            return False

    @classmethod
    def quad_residues(cls, p, verbose=False):
        """
        Prints x^2 mod p for all x = 0,1,...,p-1

        args

        p: int

        returns

        [0^2, 1^2, 2^2, 3^2, ..., p-1^2]: list of ModP
        """
        if verbose == False:
            quadratic_residues = []
            for i in range(p):
                res = cls(i,p)
                quadratic_residues.append(res.pow(2))

            return quadratic_residues
        
        if verbose == True:
            pass
    

    #returns a generator mod p
    #Very inefficient (the first time round): be warned
    #Thinking of using a dictionary, so that the program only has to run get_generator once. if it is the first time that a generator is found, 
    #then it will add it to the dictionary.
    def get_generator(p: int) -> ModP:
        pass 
        


if __name__ == '__main__':
    ''' 
    print(ModP.extgcd(7,3))
    test1 = ModP(10,17)
    test2= ModP(12,17)
    t3 = test2.inv()
    test3 = ModP(0,19)
    print(repr(t3))
    print(repr(test2.inv() * test2))
    print(repr(test1.div(test2)))
    '''


    #print(ModP(2,5).is_generator())
    """
    test1 = ModP(2,5)
    for i in range(5):
        print(test1.pow(i))

    print(test1.is_generator(print_residues = True))
    """
    
    test1 = ModP(2,5)
    print(test1.pow(4))


