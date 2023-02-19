class Bike:
    
    def __init__(self,stock):
        self.stock = stock
        
    def totalbike(self):
        print("Total Bike is -->  " ,self.stock)

    def ReturnBike(self,q):
        self.stock = self.stock+q
        print("Thanks for taking our service have a nice day ")
        print(" Now the availble bike is -->  ",self.stock)
        
    def RentBike(self,a):
        self.a = a
        if a<=0:
            print("Please enter the positive value and greater then zero")
        elif a>self.stock:
            print("Enter the value (less then stock")
        else:
            self.stock = self.stock - a
            print("Total prices",a*100)
            print("Total Bikes remaining-->",self.stock)
while(True):
    obj = Bike(100)
    uc = int(input('''
    1 Totalbike
    2 Rent a Bike
    3 Exit
    4 Return Bike        '''))
    if uc ==1:
        print(obj.totalbike())
    elif uc==2:
        b = int(input("Enter the no. of bike you want to Rent -->  "))
        obj.RentBike(b)
    elif uc == 4:
        d = int(input("Enter the bike you wnt to return --> "))
        obj.ReturnBike(d)


    


