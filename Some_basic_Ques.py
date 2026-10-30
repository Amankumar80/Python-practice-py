# Q1. Write a program to input 2 numbers and print their suM
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print(f"The sum of {a} and {b} is {a+b}.")

# Q2. Write a program to input the side of a square and print its area.
side=int(input("Enter the side of a square:"))
print(f"The area of the square is {side**2}")

# Q3. Write a program to input 2 floating-point numbers and
 # print their average.
num1=float(input("Enter 1st number:"))
num2=float(input("Enter 2nd number:"))
print(f"The avrage of {num1} and {num2} is {(num1+num2)/2}")

# Q4. Input 2 integers a and b. Print True if a is greater than or
# equal to b, otherwise print False.
a=int(input("Enter 1st input:"))
b=int(input("Enter 2nd input:"))
print(a>=b)

# Q5. Write a program to input the user's first name and print its length.

name=str(input("Enter Your Name:"))
print("length of your name is ",len(name))

# Q6. Write a program to find the occurrence of '$' in a string.
a=input("Enter a string:")
print(a.count("$"))

# Q7. Write a program to check if a number entered by the user is odd or even
num=int(input("Enter a Number:"))
if num%2==0:
    print("It is Even!")
else:
    print("It is odd!")    

# Q8. Write a program to find the greatest of 3 numbers entered by the user.
num1=int(input("Enter 1st Number:"))
num2=int(input("Enter 2nd Number:"))
num3=int(input("Enter 3rd number:"))
if num1>=num2 and num1>=num3:
    print(num1,"is Greater!")
elif num2>=num3:
    print(num2,"is Greater!")
else:
    print(num3,"is Greater!")  
if num1==num2==num3:
    print("All are equal")      

# Q3. Write a program to check if a number is a multiple of 7 or not

num=int(input("Enter a Number:"))
if num%7==0:
    print(num,"is multiple of 7")
else:
    print(num,"is not multiple of 7") 
           