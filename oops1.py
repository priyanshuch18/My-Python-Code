class Animal():
    def __init__(self, Age , breed,name):#constructor method
        print("object is created")
        self.name = name
        self.Age = Age
        self.breed=breed
    def animalDetails(self):
        print(f"the animal breed is {self.breed}")
        print(f"the animal name is {self.name}")
        print(f"the animal age is {self.Age}")
Tommy=Animal(12,"dog",'tommy') #creating object
Tommy.animalDetails()
        

