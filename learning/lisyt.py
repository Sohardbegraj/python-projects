mylist=[1,2,3,True,False,"apple","apple",2.34]
# list ordered, mutable ,duplicate values

mylist2=[1,-2,-10.4,4,55550]
for x in mylist:
    print(x)

if "cherry" in mylist:
    print("yes")
else:
    print("no")


print(len(mylist)) # give lenght of mylist = 7

print(mylist[0]) # give first element of mylist = 1
print(mylist[-1]) # give last element of mylist = 2.34


mylist.append("lemon")

mylist.insert(1,"orange")# insert orange in mylist at index 1
print (mylist)

item=mylist.pop()
# remove last item from mylist and assign it to item
print(item) # print last item of mylist

print(mylist)

mylist.remove("apple")
# remove first occurrence of "apple" from mylist
print(mylist)

mylist.reverse()
# reverse mylist
print(mylist)

mylist2.sort()
print(mylist2)
# sort mylist2 in ascending order

new_list =mylist + mylist2
print(new_list)

a=new_list[2:6]# slicing of new_list[start,end-1]
print(a)

b=new_list[::2]# copy new_list [::2 => means it take two steps]
print(b)


#copying a list
mylist4=mylist.copy()# this is deep copy 
mylist3=mylist# this is shallow copy
mylist.append(10)
# append 10 to mylist


# copy mylist to mylist4
print(mylist) # print mylist
print(mylist3) # print mylist3
print(mylist4)

mylist.clear()
# clear mylist
print(mylist)


mylist=[1,2,3,4,5]
# create a list mylist with elements 1,2,3,4,5
b=[i*i for i in mylist]
print(b)

my_list=["hello",3.4,55,True]
print(my_list + mylist)


mylist00=[1,2,3,True,False,"apple","apple",2.34]
print(mylist00[-1:-3:-1])
print("===========")
# for x in mylist00:
#     mylist00.remove(x)
#     print(mylist00)
mylist0=[99,676,535,22,555,334,111,345565,78,708,1,89,6,]
mylist0.sort(reverse=True)# sort in reverse
print(mylist0)