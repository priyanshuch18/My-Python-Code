#ENCAPSULATION(Getter and setter)
# class Student:
#     def __init__(self):
#         self.__name= ""
#     def getname(self):
#         return self.__name
#     def setname(self,name):
#         self.__name = name
# obj = Student()
# obj.setname("Testing")
# name = obj.getname()
# print(name)  
class Student:
    __name = "Ravi"
    def __init__(self):
        print(self.__name)
        self.__displayinfo()#WE can call this private function inside the class not with object directly
    def __displayinfo(self):
        print("Welcome to wscubetech")

obj = Student() 
#obj.__name() it shows error
#print(obj.__name)  # it  through error

