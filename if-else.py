'''
x = int(input("Enter No"))
if x%2==0:
    print("Even")
else:
    print("Odd")
'''
'''
x = int(input("Enter No 1:"))
y = int(input("Enter No 2:"))
z = int(input("Enter No 3:"))

if x>y and x>z:
    print(f"{x} is largest")
elif y>z:
    print(f"{y} is largest")
else:
    print(f"{z} is largest")
'''
x = int(input("Enter Side 1:"))
y = int(input("Enter Side 2:"))
z = int(input("Enter Side 3:"))
#check wether traingle is equilateral ,isoceles , scalene

if x+y>z and z+x>y and z+y>x:
    if x==y==z:
        print("equilateral")
    elif x==y or y==z or z==x:
        print("isoceles")
    else:
        print("Scalene")
else:
    print("Traingle is invalid")
