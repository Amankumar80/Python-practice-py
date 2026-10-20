# Datatypes--------------------->

# Q1. Store your age in a variable and print its type().

# My_age=int(input("What is your Age Aman ?\n"))
# print(type(My_age))

# Q2.Write a = 10, b = 3.5, c = "10" — print type()
#  of all three and understand why b and c differ.
a=10
b=3.5
c="10"
print(type(a))
print(type(b)) # since b contains decimal numbers so it's type is float
print(type(c)) # Since c contains his value in Double " " so it's type is str

# Q3 Write x = True and y = 1, then check what x == y gives and why.

X=True
Y=1
print(X==Y) # It gives True because 1 is denoted true in binary numbers or boolean expession

# print(True + True)
# print(False + 1)
# print(int(True))
# print(int(False))

# Q4. Create any complex number (in a+bj form) and print its .real and .imag.
comp=12+15j
print(comp.real)
print(comp.imag)
print(type(comp.real))
print(type(comp.imag))

# Q5.Store None in a variable, print its type(), and think about when it’s used.
a=None
print(type(a))  

#Q6.Take two numbers, print their sum, difference, product, and quotient (using /). Note whether the result of each operation is float or int.

num1=22
num2=25
sum=num1+num2
difference=num2-num1
product=num1*num2
quotient=num1/num2
print(f'sum={sum}\nDifference={difference}\nproduct={product}\nQuotient={quotient}')

# Q7. Print both 17 // 5 and 17 % 5, and explain in your own words the difference between what each one gives.

a=17
b=5
print(a//b) # It give us Quotient
print(a%b)  #It give us Remainder

#Q8. Find the result of 2 ** 5 (the power operator). Try it,
#  and also try one more: what does 2 ** 0.5 give you? 
# (Think about what operation that’s secretly doing.)

num1=2
num2=5
power=2**5 # it give us power 2 to the power 5
power2=2**0.5 # it give us power 2 to the power 0.5
print(power) # output=32
print(power2) #output=1.41421356223730951

#Q9. Compare two numbers 
# using ==, !=, >, < operators and print all four results (True/False).

A=12
B=25
print(f'{A==B}\n{A!=B}\n{A>B}\n{A<B}') 
# output:  False
        #  True
        #  False
        #  True

# Q10. Print the results of True and False, True or False, and not True.

a=True and False #output:False
b=True or False #output:True
c=not True     #output:False
print(f"{a}\n{b}\n{c}")


a=10
a+=5
a-=2
a*=3
print(a)

#Q12. Store your full name in a variable, then try both .upper() and .lower() on it.

name="Aman Kumar Chandra"
print(name.lower()) # output:aman kumar chandra
print(name.upper()) # output:AMAN KUMAR CHANDRA

# Q 13 Take a sentence, split it into words using .split(), and print the result.

Sen="Hello i'm Aman kumar I from Giridih Jharkhand and currently prusing Btech from UCET"
print(Sen.split()) 
# output:['Hello', "i'm", 'Aman', 'kumar', 'I', 'from', 'Giridih',
#  'Jharkhand', 'and', 'currently', 'prusing', 'Btech', 'from', 'UCET']


#  Q14. Clean up a string with extra spaces like " Aman Kumar " using .strip().
#  Print the result before and after stripping, so you can see the difference clearly.

Name=" Aman Kumar "
print("Before:",Name) #output: Aman kumar
print("After:",Name.strip())#output:Aman Kumar

#Q15. Use .replace() to swap one word for another in a string. For example, 
# replace “Aman” with “Kumar” (or any pair of your choice) in a sentence.

r="aman Kumar"
re=r.replace('aman','Aman')
print(re) #output= Aman Kumar

# Q16. Use .find() to get the position (index) of a word inside a sentence. 
# For example, find where “Kumar” starts in "Aman Kumar Chandra"

F="Aman Kumar Chandra"
Fi=F.find("Kumar")
print(Fi) #output:5 index

# Q17. Try string slicing: get the first 3 letters, the last 3 letters,
#  and the reversed string (using [::-1]) of any string of your choice.

a='Aman Kumar Chandravanshi'
sl=a[::-1]
print(sl) #output:ihsnavardnahC ramuK namA


# Q20. Take name and age from the user using input(),
#  and print a greeting message using both.

# Name=input("Enter your Name:")
# Age=input("Enter your Age:")
# print(f"Happy Birthday {Name}! , Now you are ofically in  {Age}")

# Q21. Take two numbers from the user (convert with int()), and find their sum.

# Num1=int(input(("Enter First Number:")))
# Num2=int(input(("Enter Second Number: ")))
# Sum=(Num1+Num2)
# print(Sum)

# Q22. Take a number from the user and print its square and cube, without using if-else.

# num=int(input("Enter Your Number:"))
# Square=num**2
# cube=num**3
# print(f"Square of your Number is {Square}\nCube of Your Number is {cube} ")

# # Q23. Take a temperature in Celsius from the user and convert it to Fahrenheit (formula: F = C*9/5 + 32).

# Temp=int(input("What is the temperature?\n"))
# frn=Temp*9/5+32
# print(f"The Actual Body Temperature is {frn}F")

# Q24. Build a simple interest calculator: take principal, rate, and time from the user, calculate and print SI (formula: SI = (P*R*T)/100).

# P=int(input("Enter Princple amount:"))
# R=int(input("Enter Rate :"))
# T=int(input("Enter Time :"))
# SI=(P*R*T)/100
# print("Simple Interst is ",SI)

# Q25. Take a sentence from the user, count total characters excluding spaces, using len() and .replace() together.

User="Hello Everyone how are you.Is Everything is fine ? "
S=len(User)
print(S)
R=User.replace("Everyone","Guys")
print(R)

# Q26. Take two strings from the user,
#  check if they’re equal (== operator), and print the result.

a=input(("Enter your 1st string...")) 
b=input(("Enter your 2nd string..."))
c=a==b
print(c)
