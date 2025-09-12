a=int(input("enter number"))

if(a>0):
    print("length is positive")
    if(a%2==0):
        print("length is even")
    else:
        print("length is odd")
elif(a<0):
    print("length is negative")
else:
    print("length is zero")