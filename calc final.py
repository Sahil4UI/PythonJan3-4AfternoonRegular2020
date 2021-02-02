def Calc(x,y,opr):
    return eval(x+opr+y)

a = (input("Enter first Number : "))
b =(input("Enter second Number : "))

choice = (input("enter operation you wanna perform : "))

res = Calc(a,b,choice)
print(res)
