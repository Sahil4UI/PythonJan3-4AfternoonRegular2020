Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Operators
>>> #arithmetical operators -> +,-,/,**,**,%,*
>>> #conditional/relational Operators
>>> #>,<,>=,<=,==(equality operator),!= (not equals)
>>> 1==1
True
>>> 5>=2
True
>>> 1!=1
False
>>> # =(Asignment operator) , ==
>>> #Assignment Operators
>>> x = 5
>>> x
5
>>> x += 1#x=x+1
>>> x
6
>>> x-=2
>>> x
4
>>> x/=2
>>> x
2.0
>>> x**=2
>>> x
4.0
>>> x %=2
>>> x
0.0
>>> #logical operators
>>> #and, or , not
>>> #and - returns true if all conditions are True
>>> 5==5 and 5>=100
False
>>> #or
>>> #or- for true, atleast one condition must be true
>>> 5==5 or 5>=1000
True
>>> #not-> compliment -> Truew->false, FAlse-True
>>> not 5==5
False
>>> #bitwise operators
>>> 23 & 13
5
>>> 23 | 13
31
>>> 13<<2
52
>>> 13<<1
26
>>> 13<<3
104
>>> ~12
-13
>>> ~-12
11
>>> #membership operator
>>> vowels = 'aeiouAEIOU'
>>> 'x' in vowels
False
>>> 'A' in vowels
True
>>> 'A' not in vowels
False
>>> #identity operator
>>> x = 1
>>> y = 1
>>> x == y
True
>>> x is y
True
>>> id(x)
1502559103280
>>> id(y)
1502559103280
>>> x= [1,2,3,4]
>>> y = [1,2,3,4]
>>> x is y
False
>>> x == y
True
>>> id(x)
1502601419712
>>> id(y)
1502601419904
>>> x
[1, 2, 3, 4]
>>> y=x
>>> id(x)
1502601419712
>>> id(y)
1502601419712
>>> x.remove(1)
>>> x
[2, 3, 4]
>>> y
[2, 3, 4]
>>> x = 5
>>> y=x
>>> x
5
>>> y
5
>>> x=5
>>> y
5
>>> x=2
>>> x
2
>>> y
5
>>> x = 456
>>> x=1
>>> y=1
>>> x is y
True
>>> x is not y
False
>>> 
