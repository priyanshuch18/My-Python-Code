myDict={
    "fast": "in a quick manner",
    "harry" : " a coder",
    "marks" : [1,4,6,],
    "anothordict" :{"Harry":"player"},
    1:2
}
#dictionary methods
print(myDict.keys())#dict_keys(['fast', 'harry', 'marks', 'anothordict', 1]) output
print(type(myDict.keys()))#<class 'dict_keys'>
print(list(myDict.keys()))#['fast', 'harry', 'marks', 'anothordict', 1]
print(myDict.values())#prinst the values of keys#dict_values(['in a quick manner', ' a coder', [1, 4, 6], {'Harry': 'player'}, 2])
print(myDict.items())#dict_items([('fast', 'in a quick manner'), ('harry', ' a coder'), ('marks', [1, 4, 6]), ('anothordict', {'Harry': 'player'}), (1, 2)])
#items print the (key,values)for all contents of dictionary
print(myDict)
updateDict = {
    "lovish":"friend"
}
myDict.update(updateDict)
print(myDict)#{'fast': 'in a quick manner', 'harry': ' a coder', 'marks': [1, 4, 6], 'anothordict': {'Harry': 'player'}, 1: 2, 'lovish': 'friend'}
print(myDict.get("harry2"))#None
print(myDict["harry2"])#showing error
print(myDict["harry"])#a coder
print(myDict.get("harry"))#a coder