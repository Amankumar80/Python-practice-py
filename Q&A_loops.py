# Q1. Print all numbers from 1 to 10, using a for loop and range().

for i in range(1,11):
    print(i)

# Q2. Print all even numbers from 1 to 20, using a for loop.

for i in range(2,21,2):
    print(i)

#Q3.Print the multiplication table of 5.

for i in range(1,11):
    print(f"5*{i}={5*i}")

# Q4 Print a countdown from 10 to 1
for cd in range(10,0,-1):
    print(cd)
# Q5. WAP to display multipliction table for n numbers up to 10

table=int(input("Enter a number:"))
for i in range(1,11):
    print(table*i)    #------> table of n number
    print(f"{table}*{i}={table*i}") #-------- multiplication table of n number

