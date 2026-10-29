# loops- 1.For loops 2.While Loops----->
# for loop---->

for i in range(1,9,1):      # range(start,stop,step)
    print("Hello Baby!")  
for i in range(9):
    print("Hello Baby!") # It takes start and step by defalut 0 so it start from 0 & steps 0

# Q. WAP to display all natural number 0 to 9 

for i in range(1,10):
    print(i)

# There are two fn in loops Break and contiue let's Dissuss:
# Break-------->
#EX-1
for i in range(1,11):
    break 
    print("i") # It display nothing because of break fn 
# EX-2
for i in range(1,11):
    if i==5:
        break # it break the line at i==5
    print(i)

# continue------->
# EX-1
for i in range(1,8):
    continue # it skip the print fn 
    print(i) 

# ex-2
for i in range(1,8):
    if i==5:
       continue  # It skip the print fn at i ==5
    print(i)

# While loop 

i=1
while i<=5:                 # it have their own condition 
    print("I'm the boss") 
    i=i+1 

# Ex with break and continue---

i=1
while i<=6:
       if i==3:
          break 
       print("Hello Aman")
       i=i+1
else:    
    print("STOP")

i=1
while i<=6:
       if i==3:
          continue
       print("Hello Aman")
       i=i+1
else:    
    print("STOP")
