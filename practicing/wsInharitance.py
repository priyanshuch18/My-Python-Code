# multi level inharitance

# class A:
#     def displayA(self):
#         print("welcome to priyanshu's worldA")
# class B(A):
#     def displayB(self):
#         print("welcome to priyanshu's world")
# class C(B):
#     def displayC(self):
#         print("p")
# obj = C()
# obj.displayA()
# obj.displayB()
# obj.displayC()
                    #MULTIPLE INHARITANCE
class A:
    def displayA(self):
        print("welcome to priyanshu's worldA")
class B:
    def displayB(self):
        print("welcome to priyanshu's world")
class C(A,B):
    def displayC(self):
        print("p")
obj = C()
obj.displayA()
obj.displayB()
obj.displayC()

