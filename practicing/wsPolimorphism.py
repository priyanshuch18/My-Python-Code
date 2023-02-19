# l = [10,20,30,40]
# print(len(l))
# s = "welcome"
# print(len(s))
# class Ws:
#     def displayinfo(self,name=''):
#         print("welcome to ws"+name)
# obj = Ws()
# obj.displayinfo() #Output = welcome to ws (paremeter does not pass while we take 'name' a parameter )[QVERLOADING CONCEPT]
# obj.displayinfo("priyanshu")
#                     #function name same peremerter diffrent
# class Ws:
#     def displayinfo(self):
#         print("welcome")
# class IIp(Ws):
#     def displayinfo(self):#function name same as ws class
#         print("welcome to IIp")
# obj =IIp()
# obj.displayinfo() #output = welcome to IIp{CONCEPT OVERRIDING}
# class Ws:
#     def displayinfo(self):
#         print("welcome")
# class IIp(Ws):
#     def displayinfo(self):
#         super().displayinfo() #super ki help se aap parent k function ko call kar sakte h jo same naam ka h
#         print("welcome to IIp")
# obj =IIp()
# obj.displayinfo() 
class Area:
    def find_area(self,x= None,y= None):
        if(x!= None and y!= None):
            print(x*y)
        elif(x!=None):
            print(x*x)
        else:
            print("nothing")
obj = Area()
obj.find_area(10)
obj.find_area(10,20)
obj.find_area()