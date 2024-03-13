#! Eg:3
#?Take values of length and breadth of a
#?from user and check if it is square or not.
'''
length=int(input())
breadth=int(input())
if length==breadth:
    print("its a square")
else:
    print("its not square")
'''
# Eg:4
#python program to check whether the given
#integer is a multiple of both 5 and 7
'''
n=int(input("enter the number:"))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")
'''
# Eg:5
#write a program to accept the cost price of bike and display the raod
#tax to be paid.
#cost price(in RS)
#>100000
1#>50000 and <=100000
#<=50000
'''
price = int(input("enter the price: "))
amount =0
if price>=100000:
    discount = price*(6/100)
    value = price-discount
    tax=value*(15/100)
    total=value+tax
else:
    tax = price*(5/100)
    total = price+tax
print("the onroad cost of bike is: ",total)
'''
#Eg:1
'''
a=7
b=9
c=3
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
else:
    print("C is greater")
'''
# A school has following rules for grading system:
# a. below 25 - F
# b. 25 to 45 - E
# c. 45 t0 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. above 80 - A
# Ask user to enter marks and print the corresponding grade.
'''
n1=int(input("enter marks"))
if n1<25:
    print("F")
elif n1>=25 and n1>=45:
    print("E")
elif n1>=45 and n1>=50:
    print("D")
elif n1>=50 and n1>=60:
    print("C")
elif n1>=60 and n1>=80:
    print("B")
else:
    print("pass")
'''
#-->short hand if else
#Eg:1
'''
a=66
b=60
if a>b:
    print("a")
else:
    print("b")
'''
#--> using short hand if else
#rules
#-->statement inside the if condition have to be present at first
#-->elif cannot be used in short hand if else
#--->always it have to end with else
'''
print("a") if a>b else print("b")
'''
#code to check the given char is vowel or consonant
'''
char = input("enter the char:")
if char=="a" or char =="e" or char=="i" or char=="o" or char=="u":
    print("its consonant")
else:
    print("its consonant")
'''
#-->or
'''
str1 = "aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("constant")
'''
'''
# short hand if else
char = input("enter the char:")
str1 = "aeiouAEIOU"
print("vowels") if char in str1 else print("cosonant")
#-->elif ladder using short hand if else
#Eg:1
# find greatest among 3 variables using short hand if else
a=8
b=5
c=9
print("a is greater") if a>b and a>c else print("b is greater") if b>a and b>c else print("c is greater")
'''
#--->looping
#looping can be implimented using
#for loop
#while loop
#-->for loop
#for loop is used to iteration if we know the number of times the loop have to run
#it is used to iterables eg(string,list,tuple,etc...)
#-->syntax for loop
#for syntax in c
#for(i=0;i<10;i++){
    #printf("hello");
#}
#for syntax in python
#for user defined_variable in range(start,end,step):defaut step value is 1
#    statement
#   statement
#   statement
'''
#Eg:1
# to print the value from 1 to 10 using for loop
#for i in range(0,10): #(n,n-1)
#    print("hello")

#Eg:2
#for val in range(23,50,2):
#   print(val)
#for val in range(23,50,3):
#   print(val)
'''
#Eg:3
'''
#to decrement the value
#for val in range (10,0,-1):
#   print(val)
#for val in range (10,0,-2):
#    print(val)
#Eg:4
#print the output of 7th multiplication table from 21 to 43
#for val in range (1,10+1):
#   print('7','x',val,'=',val*7)
#    ans="7 x {} = {}"
#    print(ans.format(val,val*7))
#    print("7 x ",val,"=",val*7)
#method:3
#    print(f"7 x {val}={val*7}")
'''
#Eg:5
#break-->which is used to terminate the loop or stop the loop
'''
#for val in range(1,10):
#    if val == 6:
#        break
#    print(val)
#Eg:6
#for val in range(1,10):
#    print(val)
#    if val == 6:
#        break
#Eg:7
#for val in range(1,10):
#    if val == 6:
#        print(val)
#        break
'''
# continue
#Eg:1
'''
for val in range(1,10):
    if val==6:
        continue
    print(val)
'''
#practise problems
#print the even number between 20 to 40
'''
for val in range(20,40):
    if val%2==0:


        print(val)
#print the odd number between 20 to 40
for val in range(20,40):
    if val%2!=0:
        print(val)
'''
#-->while loop
#while is used when we do not know the number of times the loop have to run
#to iterate the non iterable while loop is used
#syntax
#initialisation
#while condition:
#    statment
#    incr or decre
#Eg:1
#to iterate number from 1 to 10
#i=0
#while i<11:
#    print(i)
#     i=i+1 or I+=1
#Eg:2
#to decrement using while loop
#10,1
i=10
while i>0:
    print(i)
    i-=1
#---->assesment
#cats and mouse:hacker rank
#print the factorla of 8 using for loop
#write a program to display sum of odd numbers and even
#numbers that fall between
#12 and 37(including both numbers)
#write code to print the sum of number using

















