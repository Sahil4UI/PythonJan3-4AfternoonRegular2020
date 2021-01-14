"""
*
**
***
****
*****
"""
'''
for i in range(1,6):
    print("*"*i)
'''
'''
    *
   ***
  *****
 *******
*********
'''
'''
for i in range(1,6):
    print(" "*(5-i)+"*"*(2*i-1))
'''
#Nested Loop
'''
for i in range(1,4):
    for j in range(1,4):
        print(i,j)
'''



'''
*
**
***
****
*****
'''
'''
for i in range(1,6):
    for j in range(0,i):
        print("*",end="")
    print()#nextline
'''
"""
*****
****
***
**
*
"""
'''
for i in reversed(range(1,6)):
    for j in range(0,i):
        print("*",end="")
    print()
'''
"""
    *
   **
  ***
 ****
*****
"""
'''
for i in range(1,6):
    print(" "*(5-i),end="")
    for j in range(0,i):
        print("*",end="")
    print()
'''

'''
1
10
101
1010
10101
'''
for i in range(1,6):
    for j in range(i):
        if (j+1)%2==0:
            print(0,end='')
        else:
            print(1,end="")
    print()
    
'''
1
01
010
1010
10101
'''
x = 1
for i in range(1,6):
    for j in range(i):
        if x%2==0:
            print(0,end='')
        else:
            print(1,end="")
        x+=1
    print()






















