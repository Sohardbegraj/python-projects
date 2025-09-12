a=int(input("enter value of first length"))
b=int(input("enter value of second length"))
c=int(input("enter value of third length"))

if(a==b | b==c | a==c):
    print('it is an isocelse triangle')

if(a==b & b==c ):
    print('it is an equilatoral triangle')

if(a!=b & b!=c &a!=c):
    print('it is a scalene triangle')
