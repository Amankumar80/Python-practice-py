# 1
py='pymaster india'
upper=py.upper()
title=py.title()
fromat=("Uppercase:{} \nTitle case:{}")
fmt=fromat.format(upper,title)
print(fmt)


# Q2

Remove=' clean this ' # yaha pr remove ek varible hai 
L=len(Remove) # yaha pr L ek varible hai # Len hai wo built in function hai
S=Remove.strip()# yaha pr S ek varible hai
ARS=len(S) # ARS also a varriable who store data
print(f'length before removing the space:{L} \nWord after removing the space:{S} \nLength after removing the space:{ARS} \n SO it is verified!')
# print(independent hai ) v ek built in function hai


# Q3 

string='12345'
string2='hello123'
a=string.isdigit()
b=string2.isalpha()
print(f'All character is Digit: {a} \nAll digit is Alpha: {b} ')

# Q4
string='This is bad code with bad habits'
r=string.replace('bad','good')
print(r)

# Q5

spl='one:two:three:'
a=spl.split(':')
print('The resulting list is :',a)

# Q6

j=['Python','is','fun']
print(" ".join(j))

# Q7
p='python'
a=p.startswith('py')
b=p.endswith('on')
print(f'{a}\n{b}')

# Q8

Name= "Aman Kumar"
ra=Name.rjust(30) # rjust() it align string on right side 
print(ra)

# Q9

string='7'
zeropadding=string.zfill(4)
print(zeropadding)

# Q10
intro='My name is X and my score is Y.2f'
X='Aman kumar'
Y='90.50%'
print(f'My name is {X} and my score is {Y}.')

# Q11

code='PyMaster India'
a=code.find('India')
b=code.index('India')
print(f'Find is {a}\nIndex is {b}')

# Q12
Fruit="banana"
cnt=Fruit.count('an')
cntt=Fruit.count('a')
print(f"The Number of an is:{cnt}\nThe number of a is {cntt}")

# Q13
csv="Aman,21,varanasi,Python"
s=csv.split(',')
print('\n'.join(s))

# Q14

# Q15
strip='***hello world***'
result=strip.strip('*')
print(result)

# Q16

# Q17
swap="Pymaster India"
r=swap.swapcase() # .swapcase() is used to capatialize lower letter and trun the small letter in capital vice versa
print(r)

#18

# Q19
split='a::b::c'
b=split.split('::')
print('|'.join(b))

# Q20
num=1234567.89
print(f'{num:,.2f}')

# Q21
