class Employee:
    company = "google"
    def showDetails(self):
        print("this is an employee")
class Programmer(Employee):
    language= "Python"
    def getName(self):
        print(f"the language is{self.language}")
    def showDetails(self):
        print("this is an programmer")
e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)

