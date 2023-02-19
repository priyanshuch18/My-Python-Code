num=int(input("enter the no."))
f=1
# while num>1:
#     f *=num
#     num -=1
# print("the factorial of the no.is ",f)
# same program using for loop
for i in  range(1,num+1):
    f=f*i
print("the factorial of the number is ",f)
