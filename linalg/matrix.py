"""
Wishlist:
-Numerical Linear Algebra
-Random Matrices (with values distributed according to a specified distribution)
-Fast Multiplication
-Stochastic Matrices?
"""

import random
import copy 

class Matrix:
    def __init__(self, m,n):
        """
        Initialise a matrix object of zeros. Will add other constructors later.
        """
        self.m = m
        self.n = n
        self.matrix = [[0 for i in range(n)] for j in range(m)] 

    def __setitem__(self, i,j, x):
        """
        Set item method.
        """
        assert isinstance(i, int)
        assert isinstance(j ,int)
        self.matrix[i][j] = x

    def __getitem__(self, i,j):
        """
        Get item method.
        """
        return self.matrix[i][j]

    def to_string(self):
        """
        Returns a string representation of the matrix.
        """
        res = ''
        for row in self.matrix:
            res += str(row)+'\n'

        return res.rstrip()

    def __str__(self):
        return self.to_string()

    def randomint_matrix(self,a,b):
        """
        Fills a matrix of random integers between a and b
        """
        for i in range(self.m):
            for j in range(self.n):
                self.matrix[i][j] = random.randint(a,b)

        return self 

    def __add__(self, other):
        """
        Returns the matrix self + other
        """
        if self.m != other.m:
            raise ValueError("Dimensions must agree!")

        if self.n != other.m:
            raise ValueError("Dimensions must agree!")

        res = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                res.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return res
    """
    Wishlist:
    -Numerical Linear Algebra
    -Random Matrices (with values distributed according to a specified distribution)
    -Fast Multiplication
    -Stochastic Matrices?
    -LU Decomp
    -QR Decomp
    -Eigenstuff
    """

if __name__ == '__main__':
    m1 = Matrix(4,3)

    print(m1)
    m1.randomint_matrix(1,10)
    print(m1)

    m2 = Matrix(2,2)
    m3 = Matrix(2,2)
    m2.randomint_matrix(1,4)

    print(m2)
    print(m2+m3)
