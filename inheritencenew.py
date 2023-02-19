class employee:
    company = "google"
    def showDetails(self):
        print("this is an employee")
class programmer(employee):
    name = "priyanshu"
    language  = "python"
    def getLanguage(self):
        print(f"the language is {self.language}")
    def showDetails(self):#overriting
        print("this is a programmer")
priyanshu = programmer()
harry = employee()
print(priyanshu.company)
print(priyanshu.name)
print(harry.company)
priyanshu.getLanguage()
priyanshu.showDetails()