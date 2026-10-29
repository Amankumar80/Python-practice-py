# Q1. Take two numbers from the user and check if they are equal, using if-else.
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
if num1==num2:
    print("They are equal.")
else:
    print("They are not equal.")
# Q2. Take a number from the user and print whether it is positive, negative, or zero.
num=float(input('Enter anumber:'))
if num>0:
    print("It is Positive!")
elif num<0:
    print("It is Negative!")
elif num==0:
    print("It is Zero!")    

#Q3. Take a string from the user and check whether it’s an empty string or not.
emp=str(input("Enter a string :"))
if emp=="":
    print("It is an empty string")
else:
    print("It is not an empty string")    
#Q4.Take marks of a student (0-100) and print the grade (A/B/C/Fail).
Marks=float(input("Enter your Marks:"))
if Marks>100 or Marks<0:
    print("Invalid Marks")        
elif Marks>=90:
    print("Grade A")
elif Marks>=70:
    print("Grade B")    
elif Marks>=60:
    print("Grade C")
else:
    print("Fail")    
# Q5. Take a character from the user and check whether it is a vowel or a consonant.

ch=str(input("Enter a Character:")).lower()
match ch :
    case "a":
        print("vowel")
    case "e": 
        print("Vowel")  
    case "i":
        print("vowel")
    case "o":
        print("vowel")
    case "u":
        print("vowel")
    case _:
        print("Consonent")
# Q6. Take two numbers and print the greater one.
num1=int(input("Enter the 1st Number:"))
num2=int(input("Enter the 2nd Number:"))
if num1>num2:
    print(num1,"is Greater")
else:
    print(num2,"is Greater")        
# Q7. Take a string from the user, convert it to uppercase, then check if it equals “PYTHON”.
st=str(input("Enter a string:")).upper()
match st:
    case "PYTHON":
        print("yes Equal")
    case _:
        print("Not Equal")    

# Q8. Take a number and check if it is divisible by both 2 and 3, only one of them, or neither.
num=int(input("Enter a Number:"))
if num%2==0 and num%3==0:
    print("Divisible by both")
elif num%2==0 or num%3==0:
    print("Divisible by only one")  
else:
    print("Neither divisible by  2 & 3")     
# Q9. Take a year from the user and check if it’s a leap year.
year=int(input("Enter a year:"))
if year%4==0:
    if year%400==0 or year%100!=0:
        print("Leap Year!")
    else:
        print("Not a leap year")   
else:
    print("Not a leap year")        
# Q10. Take a day number (1-7) from the user, and print whether it’s a “Weekday” or “Weekend”.
day=(input("Enter Day number"))
match day:
    case "1":
     print("weekday")
    case "2":
     print("weekday")
    case "2":
         print("weekday")
    case "3":
         print("weekday") 
    case "4":
         print("weekday") 
    case "5":
         print("weekday")
    case "6":
         print("weekend")  
    case "7":
         print("weekend")    
    case _:
         print("Ivalid Number")              