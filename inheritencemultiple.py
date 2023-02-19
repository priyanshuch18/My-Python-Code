class employee:
    company = "google"
class freelancer:
    company = "fiver"
    level = 1
    def upgradelevel(self):
        self.level=self.level+1
class Programmer(employee, freelancer):
    name = "rohit"
p = Programmer()
p.upgradelevel()
print(p.level)