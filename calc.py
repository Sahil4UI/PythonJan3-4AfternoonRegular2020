def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

a = int(input("Enter first Number : "))
b = int(input("Enter second Number : "))
print('''
press + for addition
press * for mul
press / for div
press - for sub''')
choice = (input("enter operation you wanna perform : "))
d = {"+":add , "-":sub , '*': mul , '/':div}
res = d[choice](a,b)
print(res)
