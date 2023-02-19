import json
# d = { 
#     'course_name':'python',
#     'fees': 15000
# }
# f = json.dumps(d)
# print(f)
#CONVERT JSON TO PYTHON OBJECT

# x = '{"cname": "python", "fees": 1200, "duration":"2 Month"}'

# y = json.loads(x)
# print(y)
# for a in y:
#     print(y[a])

# WRITING AND READING IN JSON
file = open("posts.json","r") #post.json is a file which is not here so this so error but its ok code is right
x = file.read()
finaldata = json.loads(x)
print(finaldata)
