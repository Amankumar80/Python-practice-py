# Write a program: input a number, print whether it is Positive, Negative, or Zero.

Num=int(input("Enter a Number:"))
if Num>0:
    print("It is Positive!")
elif Num<0:
    print("It is Negative!") 
if Num==0:
    print("It is Zero!")     

# Build a simple ATM check: if withdrawal amount <= balance → success, else → 'Insufficient funds'

Balance=80000
Amount=int(input("Enter Your amount:"))
if Amount<=Balance:
    print("Withdrawal Successfull!")
else:
    print("Insufficent Balance!")    

# WAP for trafic light which colour indicate what to do ?

trafic=input("Enter Clour in trafic signal:")
match trafic:
    case "Red" |"red"|"RED":
        tra=trafic.lower()
        print("STOP!")
    case "Yellow"|"yellow"|"YELLOW":
        print("START ENGINE!")
    case "Green"|"green"|"GREEN":
        print("NOW GO!")
    case _ :
        print("Invalid Colour!")    

# 2nd Method to solve this Question----->

trafic=input("Enter Clour in trafic signal:").lower()
match trafic:
    case "red":
        print("STOP!")
    case "yellow":
        print("START ENGINE!")
    case "green":
        print("NOW GO!")
    case _ :
        print("Invalid Colour!") 
          
#Aman is building a calendar application.
#  Given a year as input, help him determine whether it is a leap year.

year=int(input("Enter the Year:"))
if year%4==0:
    if year%400==0 or year%100!=0:
      print("It is Leap year Baby!")
    else:    
      print("It is not a leap year baby!")          
else:
 print("It is not a leap year baby!")

#  Q. Take a number from the user and check whether it is divisible by both 3 and 5, or divisible by either 3 or 5 (but not both), or divisible by neither. Print one of: “Divisible by both”, “Divisible by one”, or “Divisible by neither”.

num=int(input("Enter a number:"))
if num%3==0 and num%5==0:
    print("Divisible by Both")
elif num%3==0 or num%5==0:
    print("Divisible by one")
else:
    print("Divisible by nither")
    
                       
