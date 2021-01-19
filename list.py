Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list - list is python's mutabler data collection
>>> #mutable**
>>> #mutable-which can be changed -  insert , update , delete
>>> x=[1,2,3,4,5,"sahil",67.54,True]
>>> x
[1, 2, 3, 4, 5, 'sahil', 67.54, True]
>>> x[0]
1
>>> x[-1]
True
>>> x[::-1]
[True, 67.54, 'sahil', 5, 4, 3, 2, 1]
>>> x=[[1,2,3,[4,5,6,[7,8,9,[10,11,12]]]]]
>>> x
[[1, 2, 3, [4, 5, 6, [7, 8, 9, [10, 11, 12]]]]]
>>> x[0]
[1, 2, 3, [4, 5, 6, [7, 8, 9, [10, 11, 12]]]]
>>> x[0][3][3][1]
8
>>> x[0][3][3][3][1]
11
>>> x
[[1, 2, 3, [4, 5, 6, [7, 8, 9, [10, 11, 12]]]]]
>>> x[0]
[1, 2, 3, [4, 5, 6, [7, 8, 9, [10, 11, 12]]]]
>>> x[-1]
[1, 2, 3, [4, 5, 6, [7, 8, 9, [10, 11, 12]]]]
>>> x[-2]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x[-2]
IndexError: list index out of range
>>> #slicing
>>> x=[1,2,3,4,5]
>>> x[::-1]
[5, 4, 3, 2, 1]
>>> x[3:]
[4, 5]
>>> x[:4]
[1, 2, 3, 4]
>>> #list methods
>>> x=[]
>>> x.append(11)
>>> x
[11]
>>> x.append(12)
>>> x
[11, 12]
>>> x.append(13)
>>> x
[11, 12, 13]
>>> x.insert(0,"hi")
>>> x
['hi', 11, 12, 13]
>>> x.insert(4,"hi")
>>> x
['hi', 11, 12, 13, 'hi']
>>> #updation
>>> x
['hi', 11, 12, 13, 'hi']
>>> x[-1]="hello"
>>> x
['hi', 11, 12, 13, 'hello']
>>> #deletion
>>> x
['hi', 11, 12, 13, 'hello']
>>> x.pop()
'hello'
>>> x
['hi', 11, 12, 13]
>>> x.pop(2)
12
>>> x
['hi', 11, 13]
>>> x.remove('hi')
>>> x
[11, 13]
>>> x=[1,1,1]
>>> x.remove(1)
>>> x
[1, 1]
>>> x
[1, 1]
>>> del x[1]
>>> x
[1]
>>> del x[0]
>>> x
[]
>>> x=[1,2,3,4]
>>> x
[1, 2, 3, 4]
>>> x*5
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> x=[1,2]
>>> y=[3,4]
>>> x+y
[1, 2, 3, 4]
>>> x+1
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    x+1
TypeError: can only concatenate list (not "int") to list
>>> x
[1, 2]
>>> y
[3, 4]
>>> x.extend(y)
>>> x
[1, 2, 3, 4]
>>> x=[1,2]
>>> y=x.copy()
>>> x
[1, 2]
>>> y
[1, 2]
>>> id(x)
2213509088192
>>> id(y)
2213509087552
>>> x=[1,2,[3,4]]
>>> y = x.copy()
>>> x
[1, 2, [3, 4]]
>>> y
[1, 2, [3, 4]]
>>> id(x)
2213509089024
>>> id(y)
2213509152960
>>> id(x[2])
2213509088000
>>> id(y[2])
2213509088000
>>> x[2].pop()
4
>>> x
[1, 2, [3]]
>>> y
[1, 2, [3]]
>>> import copy
>>> y=copy.deepcopy(x)
>>> x
[1, 2, [3]]
>>> y
[1, 2, [3]]
>>> id(x[2])
2213509088000
>>> id(y[2])
2213509087552
>>> 
