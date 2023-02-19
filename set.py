a={1,5,2,6,4,1}
print(a)#{1, 2, 4, 5, 6} sets does not contain repetative items
print(type(a))#<class 'set'>
b={}#this syntex will create empty dictionary not empty set
print(type(b))#<class 'dict'>  it shows dictionary
# an empty set can be create by below syntex
c=set() 
print(type(c))#<class 'set'>
# set methods
# adding values
c.add(4)
c.add(5)
print(c)#{4, 5}
# list cant add in set becouse list is not hasable means you can change the content of list but in set it will not happen
