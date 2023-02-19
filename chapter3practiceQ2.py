letter= '''dear name
you are selected!
date'''
NAME=input("enter the name")
DATE=input("enter the date")
letter= letter.replace("name", NAME)
letter= letter.replace("date", DATE)
print(letter)