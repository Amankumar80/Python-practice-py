# if-else-------->

Age=int(input("Enter Your Age :"))
if Age>=18:
    print("You are eligible for voting")
else:
    print("you are not eligible for voting")

# elif----->
Age=int(input("Enter Your Age:"))
if Age>21 and Age<100:
    print("Yes You ofcourse!")
elif Age>=18 and Age<21:
    print("Welcome new Voter!")
elif Age<=16 and Age<=18:
    print("GoBack home !")


# WAP to check a number is positive, negative and zero .

num=int(input("Enter Your Number:"))
if  num>0:
    print("It is Positive")
elif num<0:
    print("It is Negative")
elif num==0:
    print("It is zero")  

#Take a number from the user and check whether it’s even or odd. Print “Even” or “Odd”.

Num=int(input("Enter a Number:"))
if Num%2==0:
    print("Even")
else:
    print("ODD")    

# Q2. Take three numbers from the user and find the largest among them, using if-elif-else.

num1=int(input("Enter Your 1st Number:"))
num2=int(input("Enter Your 2nd Number:"))
num3=int(input("Enter Your 3rd Number:"))
if num1>num2 and num1>num3:
    print("The Largest Number is",num1)
elif num2>num1 and num2>num3:
    print("The largest number is",num2)
elif num3>num1 and num3>num2:
    print("The Largest number is",num3)
elif num1==num2==num3:
    print("All are same..!")   

# Q3. Take marks (0-100) from the user and print the grade based on this scale:

# 90 and above: A
# 75 to 89: B
# 60 to 74: C
# Below 60: F

Marks= int(input("Enter Your Marks:"))
if Marks>=90:
    print("You Got Grade A")     
elif Marks>=75 and Marks<=89:
    print("You Got Grade B")
elif Marks>=60 and Marks<=74:
    print("You Got Grade C")
elif Marks<60 and Marks>0:
    print("You are Fail..")     

# Take a year from the user and check whether it’s a leap year or not.

year=int(input("Enter the year:"))
if year%4==0:
    print("This is leap year baby !")
else:
    print("Ohh This is not a leap year ! ")
