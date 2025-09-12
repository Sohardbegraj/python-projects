# set: ordered ,immutable,text representation

my_str ="hello world"
a=[]
for i in range(10,-1,-1):
    a.append(my_str[i])
# print revered string
print(a)

a.clear()

for i in my_str:
    a.append(i)
print(a)

mylist=my_str.split()
print(mylist)

b=" ".join(a)
print(b,"=>>this is b")

substring=my_str[:5] # string slicing
print(substring)

print( my_str +" "+ substring)

s="         hello  world       "
S=s.strip()
print(S) # remove extra spaces

print(S.endswith("world"))
print(S.startswith("world"))
print(S.replace("world","universe")) 

var=3.14545516
my_str="the variable is {:.2f} and this is that".format(var)
print(my_str) # format string {:.2f} means we only want 2 digit after decimal
