class Polynomial:
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
            res1 = Polynomial.degree(self.degree)
            res1.coefficients = [elem for elem in self.coefficients] 
            for i in range(len(self.coefficients)):
                res1.coefficients[i] = res1.coefficients[i] + other.coefficients[i]
            return res1
        
        if self.degree > other.degree:
            res1 = Polynomial.degree(self.degree)
            res1.coefficients = [elem for elem in self.coefficients]
            for i in range(len(other.coefficients)):
                res1.coefficients[i] = res1.coefficients[i] + other.coefficients[i]
            return res1

        if self.degree < other.degree:
            res1 = Polynomial.degree(other.degree)
            res1.coefficients = [elem for elem in other.coefficients]
            for i in range(len(self.coefficients)):
                res1.coefficients[i] = res1.coefficients[i] + other.coefficients[i]
            return res1


    def __radd__(self, other):
        pass


    def __mul__(self, other):
        res = Polynomial.degree((self.degree*other.degree))
        for i in range(0,self.degree+1):
            for j in range(0,other.degree+1):
                for k in range(0,res.degree+1):
                    if i+j == k:
                        res.coefficients[k] += self.coefficients[i]*self.coefficients[j]
                    
        return res
                

    def __rmul__(self, other):
        pass

    def __divmod__(self, other):
        #f = qg + r, return q, r (modulo and remainder)
        pass

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

    import fields.ModP as ModP

    test1 = Polynomial(coefficients=(1,2,3))

    test2 = Polynomial(coefficients=(1,2))

    a = test1 + test2
    print(repr(a))
    print(repr(test1))
    

    
        