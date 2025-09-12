b=str(input("enter value of coffient of x^2"))
c=str(input("enter value of cofficient of x"))
a=str(input("enter value of constant"))

D=b**2-4*a*c

if(D>0):
    print("roots are real and distinct")
elif(D==0):
    print("roots are real and equal")
elif(D<0):
    print("roots are imaginary")
else:
    print("invalid")
    