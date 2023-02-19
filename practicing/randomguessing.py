import random
while (True):
    a = random.randint(1,20)
    b = int(input("Enter the no."))

    if (a>b):
        print("no. is lesser then computer Try again...")
    elif(b>a):
        print("no. is greater try again")
    else:
        print("YOU WIN")
        exit()
    