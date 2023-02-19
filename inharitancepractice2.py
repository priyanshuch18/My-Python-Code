class animals:
    print("they are animals")
class pets(animals):
    print("they are breating")
class dog(pets):
    @staticmethod
    def barking():
        print("bow bow!")
barki=dog()
barki.barking()