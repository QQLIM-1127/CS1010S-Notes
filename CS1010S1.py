#CS1010S notes
# CS1010S is a module at the National University of Singapore (NUS) that focuses on programming and problem-solving skills.
# This file contains notes and code snippets for the CS1010S module.
# The notes cover various topics such as data types, control structures, functions, and algorithms.

#topic 1: If/else statements
if True and False:
    print(False)
if True and True:
    print(True)
if False and False:
    print(False)

x=True
if x: #this if line activates if x is True
    print("x is True")
else: #activates this line if x is False
    print("x is False")  

if True or False:
    print("True") # or statements work as long as one of them is a True option

#not returns True if the expression is false, and False if the expression is true.
if not True:
    print("this will not print") #not True means False
else:
    print("this prints instead of the if statement")

#if : #raises SyntaxError, if needs a following statement

#how elif works:
x=1
if x==0:
    print(x) #needs a if statement first before any line of elif 
elif x==1:
    print(x+1) #this line will run
else: #else is everything other than the if and elif statements
    x+=1
#solve not -> and -> or

y=0
if y==0: #this would run
    y+=1
if y==1: #this would run too as both if statements are not indented
    y+=2  

if y==0:
    print(y)
    if y==1: #this would be bypassed
        y=3 
    else: #this happens, so y is now 2
        y=2
