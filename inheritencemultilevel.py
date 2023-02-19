from webbrowser import get


class person:
    country = "india"
    city = "kuralicity"
    def takeBreath(self):
        print("i am breathing...")
class Employee(person):
    company = "honda"
    salary = "1000"
    def getSalary(self):
        print(f"salary is {self.salary}")
    def takeBreath(self): 
        print("i am a employee and luckily i am breathing")
class programmer(Employee):
    company= "fiver"
    def getSalary(self):
        super().takeBreath()
        print("no salary to programmer")
p = person()
e = Employee()
g = programmer()
p.takeBreath()                       
e.takeBreath()
e.getSalary()
g.getSalary()

