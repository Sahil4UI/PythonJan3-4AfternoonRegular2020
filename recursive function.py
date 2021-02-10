'''
def f1():
    print("i am inside f1")
    def f2():
        print("i am inside f2")
    def f3():
        print("i am inside f3")
    return f2,f3

x,y= f1()
x()
y()
'''

#Recursive Function
'''
def f1(x):
    if x>10:
        return
    
    f1(x+1)
    print(x)

f1(1)
'''
#factorial of given number using recursive function
'''
def fact(x):
    if x==1:
        return 1

    if x==0:
        return 0
    
    res = x * fact(x-1)
    return res


print(fact(5))
'''
def sod(x):
    if x<1:
        return 1

    rem=x%10
    res = rem + sod(x//10)
    return res

print(sod(1254))




















