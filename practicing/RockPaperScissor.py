import random

com = random.randint(1,3)
if(com == 1):
    com = "scissor"
elif(com ==2):
    com = "rock"
else:
    com = "paper"
while (True):
    p = input("Enter the value")
    if (com ==p):
        print("draw")
    if (com == "paper" and p=="scissor"):
        print("you win")
    elif(com == "rock" and p =="sissor"):
        print("you loose")
    elif(com=="paper" and p=="rock"):
        print("You loose")
    elif(com == "scissor"and p=="rock"):
        print("YOu win")
    elif(com == "scissor" and p=="paper"):
        print("YOu loose")
    elif(com == "rock" and p=="paper"):
        print("you loose")
    else:
        exit()

