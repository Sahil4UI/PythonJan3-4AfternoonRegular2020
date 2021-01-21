#store numbers from 1-10 in list

'''x= []
for i in range(1,11):
    x.append(i)
print(x)
'''
#list comprehension
'''
x = [i for i in range(1,11)]
print(x)
'''

#
#find the largest element from the list
'''
x = [-100,1,1000000,2,1000000,1000000,1000000,5,900,2000]
largest = -9999999999
secondLargest = -888888888
for i in range(0,len(x)):
    if x[i]>largest:
        largest,secondLargest = x[i],largest
    elif x[i]>secondLargest:
        secondLargest = x[i]
        
print(largest)
print(secondLargest)
'''
'''
x = [-100,1,1000000,2,1000000,1000000,1000000,5,900,2000]
y=[]
for i in range(0,len(x)):
    if x[i] not in y:
        y.append(x[i])
print(y)
'''
#sort the list in ascending order
'''
x = [1,89,23,98,34,-100,20]

for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if x[i] > x[j]:
            x[i],x[j] = x[j],x[i]
print(x)
'''
'''
x = [1,89,23,98,34,-100,20]

user = int(input("Enter Number :"))

if user in x:
    print("Found")
else:
    print("Not Found")
'''
#linear Search & binary Search,
#linear Search
x = [1,89,23,98,34,-100,20]
'''
for i in range(0,len(x)):
    if user == x[i]:
        print(f"{user} found at {i}")
        
        break
else:
    print("Not found")
'''
#binary Search
#list must be sorted
x = [1,89,23,98,34,-100,20]
user = int(input("Enter Number :"))
x.sort()
left =0
right = len(x)-1
while left<=right:
    mid = (left+right)//2

    if user > x[mid]:
        left = mid+1

    elif user == x[mid]:
        print(f"{user} found at {mid}")
        break
    else:
        right = mid-1
        
else:
    print("value not found")

