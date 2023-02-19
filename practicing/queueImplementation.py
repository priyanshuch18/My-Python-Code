l = []
while True:
    c = int(input(''' enter the choice
    1 enqueue
    2 dequeue
    3 front
    4 rear
    5 Exit
    '''))

    if(c == 1):
        d = int(input("enter the no."))
        l.append(d)
    elif(c == 2):
        if len(l)== 0:
            print("list is empty")
        else:
            l.pop(l[0])
    elif(c == 3):
        print(l[0])
    elif(c == 4):
        print(l[-1])
    elif(c ==5):
        exit()
    else:
        print("choice is invalid")
        print(l)
        exit()
