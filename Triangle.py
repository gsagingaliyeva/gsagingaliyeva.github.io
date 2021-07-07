class Triangle ():
    def __init__(self,a,b,c):
        self.lengthside1 = a
        self.lengthside2 = b
        self.lengthside3 = c
    
    def perimeter(self):
        return self.lengthside1+self.lengthside2+self.lengthside3

    def area(self):
        p=0.5*self.perimeter()
        return (p*(p-self.lengthside1)*(p-self.lengthside2)*(p-self.lengthside3))**0.5
    
    def scale(self,scale_factor):
        return Triangle (scale_factor*self.lengthside1, scale_factor*self.lengthside2, scale_factor*self.lengthside3)

    def is_valid(self):
        if self.lengthside1+self.lengthside2>self.lengthside3 and self.lengthside1+self.lengthside3>self.lengthside2 and self.lengthside2+self.lengthside3>self.lengthside1:
            return True
        else: 
            return False

    def is_right(self):
        if self.lengthside3**2==self.lengthside1**2+self.lengthside2**2:
            return True
        elif self.lengthside2**2==self.lengthside1**2+self.lengthside3**2:
            return True
        elif self.lengthside1**2==self.lengthside2**2+self.lengthside3**2:
            return True
        else:
            return False


t= Triangle(3,4,5)
print (t.area(), t.perimeter(), t.is_valid(), t.is_right())
print(t.scale(3).lengthside1)
    
