from abc import ABC, abstractmethod
import math

class DiscreteDistribution(ABC):
    """An abstract discrete distribution class"""

    @abstractmethod
    def mean(self):
        """Returns the expectation of the discrete rv"""

    @abstractmethod
    def cdf(self, x):
        """Returns the cdf up to x of the discrete distribution"""

    @abstractmethod
    def mode(self):
        """Returns the mode of the distribution"""

    @abstractmethod
    def variance(self):
        """Returns the variance of the distribution"""

    @abstractmethod
    def skewness(self):
        """Returns the skewness of the distribution"""

    @abstractmethod
    def kurtosis(self):
        """Returns the kurtosis of the distribution"""

class Bernoulli(DiscreteDistribution):
    def __init__(self, p):
        self.p = p
        if self.p >= 1 or self.p <= 0:
            raise ValueError("p must be between 0 and 1!")

    def mean(self):
        return self.p 

    def cdf(self, x):
        if x == 0:
            return 1-self.p
        if x == 1:
            return 1

    def mode(self):
        pass

    def variance(self):
        return self.p - math.pow(self.p, 2)

    def skewness(self):
        pass

    def kurtosis(self):
        pass

class Binomial(DiscreteDistribution):
    def __init__(self, n: int, p: float):
        self.p = p
        self.n = n
        if self.p >= 1 or self.p <=0:
            raise ValueError("p must be between 0 and 1!")
        
        
    def mean(self):
        return self.n * self.p
