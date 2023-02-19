#use open funtion to read the content of the file
f= open('sample.txt','r')
# data= f.read()
data= f.readline()# read only one line
print(data)
data= f.readline()#read anothe nextline with previous line
# data= f.read(5) read first five character from text
print(data)
f.close()