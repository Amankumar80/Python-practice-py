Name=input("What is your name?")
print("My name is ",Name)
job=input("What are you Doing Now ?")
print("I'm a ",job)


# Q1 
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print("The Sum Of these two number is :",a+b)


a=bool(input("Enter the your number:"))
print(f"{a},{type(a)}")

# Program
# Take radius from user and give him teh area of cricle 

Radius=float(input("What is your radius:"))
Area=3.1459*Radius*Radius
print(f"The area of circle is {Area}")

# Take temprature in celsius from the user and give him back to term in fanheit
Temp=float(input("What is  Temperature?\n"))
F=Temp*9/5+32
print("The temprature in Farnheit is ",F)

# Take a total seconds from user and give him in hours and minute

Sec=float(input("Total Seconds are: "))
Hrs=Sec/3600
Min=Sec/60
print(f"The time is {Hrs} hours and {Min} minutes ")

# Math Module (Mthodes in math )
import math
a=625
print(math.sqrt(a)) # It is used to find who's square of given number

b=23.2
print(math.ceil(b)) # used for round off the value in upper position

c=23.7
print(math.floor(c))# used for round of in lower position 

d=math.pi # used for finding the value of pi 
print(d)
#math.factroial
e=10
factorial=math.factorial(e) # used for finding factorial
print(factorial)
# math.pow
x=12
y=3
z=math.pow(x,y) # used for finding power of x to the power y
print(z)

# math.isclose

f=0.4
m=0.3
j=0.7
print(math.isclose(f+m,j)) # it tell us value is closed or not to the result

a=int(input("Enter the number:"))
b=math.sqrt(a)
print(b)
