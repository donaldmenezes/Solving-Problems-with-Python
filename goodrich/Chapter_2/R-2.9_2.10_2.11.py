class Vector:
    
    def __init__(self, d):
        self.coords = [0] * d
        
    def __len__(self):
        return len(self.coords)
    
    def __getitem__(self, j):
        return self.coords[j]
    
    def __setitem__(self, j, val):
        self.coords[j] = val
        
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(result)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        return self.coords == other.coords
    
    def __ne__(self, other):
        return not self == other
    
    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'
    
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(result)):
            result[j] = self[j] - other[j]
        return result
    
    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result
    
    def __radd__(self, other):
        return self.__add__(other)
        #return Vector(other + self.coords)
        
    def __mul__(self, factor):
        if isinstance(factor, Vector):
            if len(self) != len(factor):
                raise ValueError("dimensions must agree")
            else:
                length = len(self)
                result = Vector(len(self))
                for i in range(length):
                    result[i] = self[i] * factor[i]
                return result
        else:    
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] * factor
            return result
    
    def __rmul__(self, other):
        return self.__mul__(other)
