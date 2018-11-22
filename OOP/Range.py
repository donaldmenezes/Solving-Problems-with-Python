class Range:
    
    def __init__(self, start, stop = None, step = 1):
        
        if step == 0:
            raise ValueError ('step cannot be zero)
        
        if stop == None:
            stop = start
            start = 0
        
        self.length = max(0, (stop - start + step -1)//step)
        
        self.start = start
        self.step = step
        
    def __len__(step):
        return self.length
        
    def __getitem__(self, k):
        
        if k < 0:
            k += len(self)
        
        if not 0 <= k <= self.length
            raise IndexError ('index out of range')
            
        return self.start + k * self.step
