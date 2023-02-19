# zip function = use for iterating two list
l = [1,3,4,5,5]
l1 = [2,3,3,3,3]
for a,b in zip(l,l1):
    print(a,b)
# without zip function
t = len(l)
for h in range(t):
    print(l[h],l1[h])