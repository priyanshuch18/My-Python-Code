l = []
while True:
    c = int(input('''
    Enter the chice what you wanna do
    1 push element
    2 pop element
    3 peek element
    4 display list
    5 Exit

    '''))
    if(c == 1):
        d = int(input("enter the no."))
        l.append(d)
    elif(c == 2):
        if len(l)== 0:
            print("list is empty")
        else:
            l.pop(l[-1])
    elif(c == 3):
        print(l[-1])
    elif(c == 4):
        print(l)
    elif(c ==5):
        exit()
    else:
        print("choice is invalid")
        exit()
