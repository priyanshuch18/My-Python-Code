# split method = used to convert string  into list
string = "priyanshu 22"
list1 = string.split() #split the string from space
string2 = "priyanshu,22"
list2 = string2.split(",") #split the string from ,
print(list1)
print(list2)
name ,age = input("enter the name and age").split()
print(name)
print(age)