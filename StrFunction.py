# CASE METHOD 

# 1.Upper Case method 

Char="Hey Aman Chandravasnhi"
Upper=Char.upper()  # .upper() is use to capatilzed all the letters in strings. 
print(Upper)

# 2. Lower Case Method

Char="Hey Aman Chandravasnhi"
Lower=Char.lower() # .lower() is use to small all the letters in strings. 
print(Lower)

# 3. tile case 

Char="hey aman chandravasnhi"
Title=Char.title() # .title() is used to capatalized first letter of each word.
print(Title)

# 4. capatalize case 

Char="hey aman chandravasnhi"
capital=Char.capitalize() # .capitalize() is used to Cpaital first very first letter of word
print(capital)

# 5. Swapcase 
char="hey AMAN chandravanshi"
Swap=char.swapcase() # .swapcase() is used to flip lower to upper & vice versa 
# (JO BADA HAI USKO CHHOTA KREGA OR JO CHHHOTA HAI USKO BADA KREGA ) 
print(Swap)

#STRIP METHOD 

a="  Aman kumar  "
strip=a.strip() # .strip() is used to reduce the space & any sign to first and last of the string
print(strip)

b="***Aman***"
strip=b.strip('*')
print(strip)

#  SEARCH METHOD or FUNCTION 

# .find() function 

a="Hey I am Aman kumar I'm a Backend Engenieer I also works on data role "

b=a.find('I') # (It is use to search the indexing of the string)
print(b)

b=a.find('I',5)# It is use to search the indexing 5
print(b)

b=a.find('I',21)# It is use to search the indexing 21 
print(b)

b=a.find('Backend')
print(b)

b=a.find('java') # If string is not present it returns -1
print(b)

#  .index() method 

c='Hello My name is Aman kumar Chandravanshi Aman '
d=c.index('Aman')
print(d)

d=c.index("Aman",18)
print(d)

# d=c.index('python') # If string is not persent then it returns "valueError"
# print(d)

# .count() Method 

cout="Hello Aman whats going on and Aman tell me about your self me is not coming me and me "
lout=cout.count("Aman") # It is used to count how many times value is come in given string
print(lout)

print("AMANAMANAMANAMANAMANMANAAMAN".count("AMAN"))

# F-STRING FORMATING

name="AMAN KUMAR"
rank=100
print(f"Name:{name}")