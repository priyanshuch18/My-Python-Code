class complex:
    def __init__(self,i,r):
        self.imaginary =i
        self.real = r
    def __add__(self,c):
        return complex(self.real + c.real,self.imaginary+c.imaginary)
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"

c1 = complex(1,3)
c2 = complex(1,5)
print(c1+c2)