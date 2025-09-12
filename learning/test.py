# for i in range(1,21):
#     print((i*117-1 )/9)

if(1==True):
    print("hii")
else:
    print("hello")  # this is not a good practice to use number in if condition


x=10
y=10
# this is not a good practice to use same variable name for different purpose
# it is better to use different variable name for different purpose

print(x is y)
y=y+5
print(x is y)

print(id(x))
print(id(y))# x and y point to same location

# (is) and (is not) not work in case of collection

st1="hello world"
st2=" "
print(st2.join(st1))