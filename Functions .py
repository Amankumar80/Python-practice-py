# def printName(): 
# 	print('hello Alexa how are you, I hope you are doing good') 
 
# printName()

def calculate(a,b): 
	print('sum:',a+b) 
	print('subtraction:',a-b) 
	print('multiplication:',a*b) 
	print('division:',a/b) 
 
calculate(40,20) 
calculate(50,5) 
 
def wish(): 
	print('Hello Taylor ,how are you') 
 
wish() 
 
def printName(a): 
	print('hello',a,'how are you, I hope you are doing good') 
 
printName('Taylor') 
 
def printSquare(n): 
	return n*n 
 
print(printSquare(5))
def printSquare(n): 
	return n*n 
 
print(printSquare(101))

def f1(): 
	print('hello') 
 
x = f1() 
print('the return value:',x)

# Def get_age(a):
#    If a >= 18:
#        return “Adult”
#    else:
#       return “Minor”

# def get_age(a):
#    if a >= 18:
#        return "Adult"
#    else:
#        return "Minor"

#     print("Thanks for confirming")


def get_age(a):
   if a >= 18:
       return "Adult"
   else:
       return "Minor"
   print("Thanks for confirming")

print(get_age(20)) 

def factorial(n):
    result = 1

    while n >= 1:
        result = result * n
        n = n - 1

    return result
for i in range(1,6): 
	print('factorial of ',i ,'is:',factorial(i))
