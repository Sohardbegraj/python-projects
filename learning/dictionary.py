# dictionary: key-value pair, unordered,mutable

mydict={"name":"sohard","age":20}
print(mydict)

mydict2=dict(name="piyush",age=21)
print(mydict2)

value=mydict["name"]
print(value)

mydict["email"]="sexyboyhard@xyz.com"
print(mydict)

del mydict["email"] #delete email key-value pair
print(mydict)

mydict2.popitem()
print(mydict2)

try:
    mydict["city"]="delhi"
    print(mydict["country"])
except KeyError:
    print("Key not found")

for key,value in mydict.items():
    print(key,value) 

#copy dict
mydict3=mydict.copy()
print(mydict3)


my_dict={"name":"sohard","age":20,"email":"sohard16begraj@gmail.com"}
my_dict2=dict(name="mary",age=29,city="usa")

my_dict.update(my_dict2)
print(my_dict)
print(my_dict2)

#key must be mutalble i.e. cannot change with time thats why even tuple,interger(any numeric data type) can be key but {list} cannot be used as keys
