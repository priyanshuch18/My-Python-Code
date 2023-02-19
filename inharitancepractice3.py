class employee:
    salary = 20000
    increment = 1.5
    @property
    def salaryinc(self):
        return self.salary*self.increment
    @salaryinc.setter
    def salaryinc(self,salaryinc):
        self.increment=salaryinc/self.salary
e = employee()
print(e.salaryinc)
print(e.increment)
e.salaryinc= 40000
print(e.increment)
