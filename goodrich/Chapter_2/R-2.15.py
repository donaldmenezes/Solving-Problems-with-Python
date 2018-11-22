class Vector(object):
    def __init__(self, d):
        if isinstance(d, int): 
            self.values = [0] * d
        else:
            try:
                self.values = [i for i in d]
            except TypeError:
                raise TypeError ("invalid parameter type")
            
    def __str__(self):
        return '<' + str(self.values)[1:-1] + '>'
