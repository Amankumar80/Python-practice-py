# Nested Conditions------------->

# Take three numbers from the user and print the largest among them.

num1=int(input("Enter first Number:"))
num2=int(input("Enter Second Number:"))
num3=int(input("Enter Third Number:"))                

if num1>=num2:
    if num1>=num3:
        print("num1 is Greater !")
    else:
     print("num3 is Greater!")
else:
   if num2>=num3:
      print("num2 is Greater!")
   else:
      print("num3 is Greater!") 


# ONE LINE if---------->(Ternary Expression)

Score=int(input("Enter Your Score:"))
print("Pass"if Score>=40 else "Fail" )

# Match case ----->
# Q. Take a single character input from the user representing a day number (1-7), 
# and use a match-case statement to print the day name 
# (1 → “Monday”, 2 → “Tuesday”, ... 7 → “Sunday”). For any other input, print “Invalid day”.

Day_num=(input("Enter a Number of Day:"))
 
match Day_num: 
   case "1":
      print(f"{Day_num} is Sunday!!")
   case "2":
      print(f"{Day_num} is Monday")
   case "3":
      print(f"{Day_num} is Tuesday") 
   case "4":
      print(f"{Day_num}is Wednesday")
   case "5":
      print(f"{Day_num} is Thrusday")  
   case "6":
      print(f"{Day_num}is Friday")
   case "7":
      print(f"{Day_num}is Saturday")
   case _:
      print("invalid!")   
