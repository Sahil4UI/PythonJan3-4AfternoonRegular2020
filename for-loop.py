Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1,11):
	print(i)

1
2
3
4
5
6
7
8
9
10
>>> for i in range(1,11,2):
	print(i)

1
3
5
7
9
>>> for i in range(10,1,-1):
	print(i)

10
9
8
7
6
5
4
3
2
>>> for i in range(10,0,-1):
	print(i)

10
9
8
7
6
5
4
3
2
1
>>> for i in reversed(range(1,11)):
	print(i)

10
9
8
7
6
5
4
3
2
1
>>> for i in range(5):
	print(i)

0
1
2
3
4
>>> for i in range(11,21):
	print(i)

11
12
13
14
15
16
17
18
19
20
>>> for i in range(1,11):
	print(f"2X{i}={2*i}")

2X1=2
2X2=4
2X3=6
2X4=8
2X5=10
2X6=12
2X7=14
2X8=16
2X9=18
2X10=20
>>> #break
>>> for i in range(1,100000001):
	print(i)
	if i==10:
		break

1
2
3
4
5
6
7
8
9
10
>>> for i in range(1,5):
	print(i)
	if i==2 or i==3:
		continue

1
2
3
4
>>> for i in range(1,5):
	if i==2 or i==3:
		continue
	else:
		print(i)

1
4
>>> 
