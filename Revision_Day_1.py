# Revision Day 1 ------------------------->

# Data Types in python

# Integer
X=20
print(type(X)) # oputput:<class 'int'>

#Float 
Y=30.12
print(type(Y)) # Output:<Class 'float'>

# String
Z="Aman Kumar"
print(type(Z)) # output:<class 'str'>

# Boolean 
A=True
print(type(A)) # output:<class 'bool'>

#None 
B=None
print(type(B)) # output:<class 'NoneType'>

#Complex 
C=12+15j # here j is imagenary part.
print(type(C))  # output:<class 'complex'> 

# End------------------------------------------------------------------------>

# Operators --------->

# Airthmetic operator(+,-,*,/ etc.)
a=12+13-1*4//2
b=7
c=2
print((a+b)/c)   #output: 15.0(/= It is a true divsion Always gives result in float)
print((a+b)//c) #output: 15(//= It gives us floor division Gives result in integer(if both input are int))

# Assignment Operators(=,+=,-= etc.)
a=24
a+=12
print(a) # output:36
b=12
b-=12
print(b)  # output:0
c=12
c*=12
print(c)  # output:144
d=12
d/=6
print(d)   # output:2.0

# comprasion operator (==,>=,<=,!= etc)
a=12==12
print(a)  # output: True
c=12>=13
print(c)  # output:False
d=14!=12
print(d)  # output:True

# logical opertor(AND,OR,NOT)
a=True or False
print(a)  # output:True
b=True and False
print(b)  # output:Fasle
c=not(True)
print(c)  # output:False 

# END----------------------------------------------------------------------->

# String Function------>
# String = It is in inbuit function in python written as .dot function 

# CaseMethod--->
# 1.upper()---

a="aman kumar"
b=a.upper()     # It capitalize all the  letter of string
print(b)        # output:Aman Kumar
#2.lower()---
low='AMAN KUMAR'
Low=low.lower()  # It convert all the letter in lower case of  string
print(Low)        # output:aman kumar 
# 3.title()---
Tit='pawan kumar'
tit=Tit.title() # It capatilize very first letter of every string
print(tit)      # output:Pawan Kumar

#4.Capitalize() 
cap="sahnawaj khatunn"
capi=cap.capitalize() #  It capitalize only very first letter of only very firt string
print(capi)           # output:Sahnawaj khatunn
# 5.swapcase()
Sw="Devesh Karmali"
swap=Sw.swapcase() # It convert upper case to lower and vice versa.
print(swap)        #dEVESH kARMALI

#5.strip() method
st="  Aman Kumar     "
s=st.strip() # It remove all the extra space of the from the string 
print(s)



