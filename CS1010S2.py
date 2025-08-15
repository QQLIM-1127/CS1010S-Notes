#CS1010S2.py
#Strings, Int, float, various var types
#1. Strings
x="Hi I dont like cs1010" #anything in between " " is a string
x="1" #if string only has numbers inside, use int(var) to convert to an integer
int(x)
print(var(x)) #shows integer

x="abc"
y="abcd"
print(x+y) #output would be putting the strings side by side, so "abcabcd"

print(x*2) #output would be 2 of the strings, so "abcabc"

#difference between = and ==:
x=5 #assigns x to the number 5
if x==5:
    print(x) #== gives a true/false operation, if x is 5, the if section runs

#math component
#int+int=int
#int+float = float
#int/int=float
#float/float=float
print(5/5) #output is 1.0
print(5//5) #output is 1 
print(-5//2) #output is -3, always round down towards -ve infinity

#% operation
#a%b=a−b×floor(a/b)
print(7%3) #7 divided by 3 is 2 remainder 1, output is 1
print(-7%3) #-7 divided by 3 rounded towards -ve infinity is -3, output is -7-(3*-3)=2

#order of operation
#brackets, then power (if theres more than 2 go from right to left eg 2**3**3 would be 3**3=27, then 2**27) then */ and lastly +-


