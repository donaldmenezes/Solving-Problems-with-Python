def gcd(m,n):
    ''' Returns G.C.D. of two numbers '''
    while m % n != 0:
        old_m = m
        old_n = n
        
        m = old_n
        n = old_m % old_n
    
    return n

class Fraction(object):
    """
    A number represented as a fraction
    """
    
    def __init__(self, num, denom):
        """ numerator and denomimator are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom
    
    def __str__(self):
        """ Returns a string representation of self """
        return str(self.num) + "/" + str(self.denom)
        
    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num * other.denom + self.denom * other.num
        bott = self.denom * other.denom
        common = gcd(top, bott)
        return Fraction(top//common, bott//common)
    
    def __eq__(self, other):
        """ Returns if the two fractions are equal to each other """
        return self.num * other.denom == other.num * self.denom
        
    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction"""
        top = self.num * other.denom - other.num * self.denom
        bott = self.denom * other.denom
        common = gcd(top, bott)
        return Fraction(top//common, bott//common)
        
    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num / self.denom
        
    def inverse(self):
        """ Returns an inverse of the function """
        return Fraction(self.denom, self.num)
        
    def __lt__(self, other):
        """ Returns if self fraction is less than other fraction """
        return self.num * other.denom < other.num * self.denom
        
    def __le__(self, other):
        """ Return is self fraction is less than or equal to the other fraction """
        return self.num * other.denom <= other.num * self.denom
        
    def __ge__(self, other):
        """ Return if self fraction is greater than or equal to the other fraction """
        return self.num * other.denom >= other.num * self.denom
        
    def __gt__(self, other):
        """ Return if self fraction is greater than the other fraction """
        return self.num * other.denom > other.num * self.denom
        
    def __mul__(self, other):
        """ Return a new fraction representing multiplication """
        top = self.num * other.num
        bott = self.denom * other.denom
        common = gcd(top, bott)
        return Fraction(top//common, bott//common)
        
    def __trudiv__(self, other):
        """ Returns a new fraction representing division """
        top = self.num * other.denom
        bott = self.denom * other.self
        common = gcd(top, bott)
        return Fraction(top//common, bott//common)
        
    def get_num(self):
        """ Returns numerator of the fraction """
        return self.num
        
    def get_denom(self):
        """ Returns denominator of the fraction """
        return self.denom
        
    def __radd__(self,other):
        return __add__(other)

    def __iadd__(self,other):
        return __add__(other)

    def __repr__(self):
        return str(self.num)+"/"+str(self.den)
