import random
def gamewin(comp,you):
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp== 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("comp turn: snake(s) water(w) gun(g)")
comp=random.randint(1,3)
if comp==1:
    comp='s'
elif comp==2:
    comp='w'
elif comp==3:
    comp='g'
print("your turn:snake water gun")
you=input("enter the coice")
a= gamewin(comp,you)
if a==None:
    print('the game is tie')
elif a==True:
    print("you win")
elif a==False:
    print("comp win")
print("comp chose ",comp)


