#--->while loop
#--->break using while loop
#eg:1
#iterate from 20 to 30 and break the loop in 27
'''
method:1
i=20
while i<31:
    if i == 27:
        break
    print(i)
    i+=1
method:2
i=20
while i<31:
     print(i)
     if i == 27:
        break
     i+=1
method:3
i=20
while i<31:
    if i == 27:
        print(i)
        break
    i+=1
'''
#-->continue
'''
method:1
i=20
while i<31:
    i=i+1
    if i == 27:
        continue
    print(i)
method:2
i=20
while i<31:
    if i == 27:
        continue
    print(i)
    i=i+1
'''
#while to iterate from 12 t0 22
#find the sum of all numbers
'''
eg:1
i=12
sum=0
while i<=22:
    sum=sum+i
    i=i+1
print(sum)
eg:2
i=12
sum=0
while i<=22:
    sum=sum+i
    i=i+1
    print(sum)
'''
#find the average of values from 20 to 25
'''
i=20
sum=0
while i<=25:
    sum=sum+i
    i=i+1
    avg=sum/6
print(avg)
#2:
i=20
sum=0
count=0
while i<=30:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)
'''
#-->nested for loop
'''
for i in range(1,3+1):
    for j in range(1,4+1):
        print(i,j)
#2:
for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()
rows=int(input("enter the rows:"))
cols=int(input("enter the cols:"))
for row in range(rows):
    for col in range(cols):
        print("*",end=" ")
    print()
sum=0
for i in range(4):
    for j in range(4):
        sum=sum+1
        print(sum,end=" ")
    print()
'''
#to print stars in right angled triangle
'''
for row in range(0,6):
    for col in range(0,row+1):
        print("*",end=" ")
    print()
for row in range(6,0,-1):
    for col in range(0,row):
        print("*",end=" ")
    print()
for row in range(5):
    for col in range(5):
        if col==0 or col==4 or row==0 or row==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#-->list
#data types
'''
primary
number-->int,float,complex
string
boolean
none
'''
#collection
'''
list
tuple
set
dictionary
#-->list
1.if the collection elements are sorrounded by square brackets,it is considerd
to be list
  eg:
      L1=[4,7,9,9.89,hellow,7+9j,[3,4,5]]
'''
#-->characteristics of list
'''
1.list have to be sorrounded by[]
2.it is mutable(the elements in the list are changeable)
3.every element inside list is indexed
4.the element inside list will be ordered format
5.it can hold duplicate values
6.its heterogenous
'''
#to acces the element in list
L1=[1,4,6,1,89.6,"p","i"]
#print(L1)
#--->indexing
'''
the collection datatypes like list,tuple,string,the elements will be alloted
with predefined unique called index value
we have 2 types of indexing
positive indexing-->start with 0 from left hand side
negative indexing-->with -1 from right hand side
'''
#positive indexing
#L1=[1,4,6,1,89.6,"p","i"]
#print(L1[4])
#print(L1[20])-->error out of the list
#negative indexing
#L1=[1,4,6,1,89.6,"p","i"]
#print(L1[-1])
#print(L1[-3])
#-->slicing
#L1=[start_index:end_index:step]
'''
L1=[1,4,6,1,89.6,9,"p","i"]
print(L1[5:7])
print(L1[:5])
print(L1[5:])
print(L1[:])
print(L1[0:7:1])
print(L1[0:7:2])
print(L1[-4:-1])
print(L1[-1:-4])
print(L1[-7:-1:2])
'''
#to insert to add element inside list
#append()--->used to add element at last position of list
l1=[9,8,0,6]
l1.append("car")
print(l1)















