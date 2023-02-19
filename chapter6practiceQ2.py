sub1=int(input("enter the marks of subject1"))
sub2=int(input("enter the marks of subject2"))
sub3=int(input("enter the marks of subject3"))
if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail")
elif(sub1+sub2+sub3)/3<40:
    print("youare fail")
else:
    print('congretulation')
