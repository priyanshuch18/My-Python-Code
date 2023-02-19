num=int(input("enter the number"))
for i in range(2,num):
    if(num%i==0):
        print("this no. is not prime")
        break
    else:
        print('this no. is prime ')