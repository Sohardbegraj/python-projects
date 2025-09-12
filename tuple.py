# tuple is ordered ,immutable,allowed duplicate
tup=("max",99,"dave")
print(tup)
for i in tup:
    print(i) 

new_tup=tuple([i*i for i in range(0,11)])
print(new_tup) # prints (0, 1, 4, 9,16,25,36,49,64,81,100)

print(len(new_tup))

print(tup.count("max"))
# prints 1

print(new_tup.index(4))# index to 4 in new_tup is 2 

b=new_tup[2:8:2]
# slicing of new_tup [start,end-1,steps]
print(b)

x,*y,z=new_tup # unpacking of tuple
print(x)# first element of new_tup
print(y)# all middle element of new_tup coverted to a list
print(z)# last element of new_tup

print("*******************************")
import sys
my_list=[1,2,3,"hello",True]
my_tuple=(1,2,3,"hello",True)

print(sys.getsizeof(my_list)) #list is more in size
print(sys.getsizeof(my_tuple)) # tuple is more memory efficient than list