#reduce function
'''
from functools import reduce
def add(x,y):
    return x+y

x=[1,2,3,4,5]

res=reduce(add,x)
print(res)
'''
'''
def f1():
    for i in range(1,11):
        return i

res = f1()
print(res)
'''
'''
def f1():
    for i in range(1,11):
        yield i

res = f1()
print(next(res))
'''
#decorator
'''
def f1(f3):
    def f2():
        print("Hello i am f2")
        f3()
    return f2


def myFun():
    print("My function")


x=f1(myFun)
x()     
'''
def f1(f3):
    def f2():
        print("Hello i am f2")
        f3()
    return f2

@f1
def myFun():
    print("My function")

myFun()
