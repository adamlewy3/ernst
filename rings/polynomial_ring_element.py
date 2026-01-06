import copy 

class Polynomial:
    """ 
    Class for Polynomials with coefficients in any ring - so that multiplication, addition, and subtraction are defined
    """
    def __init__(self, coefficients):
        self.coefficients = list(coefficients)
        self.degree = len(coefficients)-1 

    @classmethod
    #returns the 0 polynomial of degree n
    def degree(cls, n: int):
        return cls([0 for _ in range(0,n+1)])

    def __repr__(self):
        #returns the string representation of a polynomial

        return "Polynomial"+str(self.coefficients)
    
    def __add__(self, other):
        if self.degree == other.degree:
            res1 = copy.deepcopy(self)
            for i in range(len(self.coefficients)):
                res1.coefficients[i] = res1.coefficients[i] + other.coefficients[i]
            return res1
        
        if self.degree > other.degree:
            res1 = copy.deepcopy(self)
            for i in range(len(other.coefficients)):
                res1.coefficients[i] = res1.coefficients[i] + other.coefficients[i]
            return res1

        if self.degree < other.degree:
            res1 = copy.deepcopy(other)
            for i in range(len(self.coefficients)):
                res1.coefficients[i] = res1.coefficients[i] + self.coefficients[i]
            return res1

    def __radd__(self, x):
        assert isinstance(x, int)
        res = copy.deepcopy(self)
        res.coefficients[0] += x
        return res
       
    def __neg__(self):
        return -1 * self

    def __sub__(self, other):
        return self  + -other

    def remove_zeros(self):
        """ 
        Removes the leading zeros of a polynomial. Returns a new polynomial with appropriate number of zeros. 
        """
        if self.coefficients[-1] != 0:
            return self
        else:
            self.coefficients.pop(-1)
            self.degree -= 1
            return self.remove_zeros()

    def __mul__(self, other):
        res = Polynomial.degree((self.degree+other.degree))
        for i in range(0,self.degree+1):
            for j in range(0,other.degree+1):
                for k in range(0,res.degree+1):
                    if i+j == k:
                        res.coefficients[k] += self.coefficients[i]*other.coefficients[j]
                    
        return res

    def __rmul__(self, x):
        res = Polynomial.degree(self.degree)
        res.coefficients = [x * i for i in self.coefficients]
        return res 

    def __divmod__(self, other):
        """ Division with remainder method. 

        self: polynomial
        other: polynomial

        return q: polynomial, r: polynomial such that
        self = q * other + r if deg self >= deg other. and q=0, r = 0 otherwise.
        """ 
        self = self.remove_zeros()
        other = other.remove_zeros()

        if self.degree <= other.degree:
            return 0, self
        
        if self.degree > other.degree:
            res = Polynomial.degree(self.degree)
            res.coefficients = [i for i in self.coefficients]
            res = other.coefficients[-1] * res
            print(res)
            
            res1 = Polynomial.degree(self.degree - other.degree)
            res1.coefficients[-1] = self.coefficients[-1]
            print(res1)

            res = res - res1*other
            res = res.remove_zeros()
            q1, r1 = divmod(res, other)
            q1 *= other.coefficients[-1]
            return q1 + res1, r1

    def __str__(self):
        def x_expression(degree):
            if degree == 0:
                res =  ""
            elif degree == 1:
                res = "x"
            else:
                res = "x^"+str(degree)
            return res
        
        degree = self.degree
        res = ""

        for i in reversed(range(0,degree+1)):
            if i > 0:
                res = res + str(self.coefficients[i])+x_expression(i) + "+"
            if i == 0:
                res =  res + str(self.coefficients[i])+x_expression(i) 
        return res.lstrip("+")
    


if __name__ == '__main__':

    test1 = Polynomial(coefficients=(1,2,3))

    test2 = Polynomial(coefficients=(1,2))

    a = test1 + test2
    b = test1 * test2
    print(f"{test1} + {test2} = {a}")
    print(f"{test1} * {test2} = {b}")


    #should return 2x+0
    #divmod(test1, test2)

    #Now this is completely broken. Awesome.
    #Should return 2x+1 - 3x^2-2x-1 = -3x^2
    """
    print(test1)
    print(test2)
    
    print(-test1)
    print(test2 + -test1)
    print(test2 - test1)        
    """
    c =test2+test1
    print(f"{test2} + {test1} = {c}")

    d = test1- test2
    print(f"{test1} - {test2} = {d}")

    e = test2 - test1
    print(f"{test2} - {test1} = {e}")

    test3 = Polynomial(coefficients=(3,1))
    q,r = divmod(test1, test3)

    f = q*test3 + r

    print(f"{test1} = {f} = {q}*{test3} + {r} ")

    poly1 = Polynomial(coefficients=(4,5,3,1))
    
    q1, r1 = divmod(poly1, test1)
    f1 = q1*test1 + r1

    print(f"{poly1} = {f1} = {q1}*{test1} + {r1}")


    pol2 = Polynomial(coefficients=(3,4,5,0,3,0,0,0))
    print(pol2.degree)
    pol3 = pol2.remove_zeros()
    print(pol3.degree)

    #pol2 = 3x^4 + 5x^2 + 4x + 3
    #pol3 = x^3 + 3x^2 + 5x + 4
    #what is divmod(pol3, pol2)?

    q2, r2 = divmod(pol2, poly1)

    f2 = q2 * poly1 + r2

    print(f"{pol2} = {f2} = {q2}*{poly1} + {r2}")


