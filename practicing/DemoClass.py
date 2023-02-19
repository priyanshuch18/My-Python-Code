class DemoClass:
    a = 10 
    def showvalue(self): # self is must when you want to derive a functio inside a class 
        print(self.a) #must take self for print class variable
        self.c = self.a*self.a
        print(self.c) #self with variable is must for variable in function
    def __init__(self): #constructor
        print("welcome to priyanshu's world")
    def showvalue2(self,a,b):
        print(a+b) # argument dont need self

obj = DemoClass()
obj.showvalue()
obj.showvalue2(20,30)
                        #WE DONT NEED TO CALL CONTRUCTOR IT CALL ITSELF WHILE MAKING THE OBJECT