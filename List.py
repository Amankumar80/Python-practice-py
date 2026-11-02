# Q1. Create a list of 5 numbers of your choice. Print the first element, the last element, and the length of the list.
num=[1,2,3,4,5]
print("First element is ",num[0])
print("Last element is ",num[4])    # num[-1] it is also the last elemnet 
print("Length  of the list is ",len(num))

# Q2. Create a list of 5 fruit names. Add one more fruit at the end,
#  insert one fruit at position 1, and print the final list.
fruits=["Mango","Banana","Apple","Srawberry","Cocowa"]
print(fruits)
fruits.append("pine apple")
print(fruits)
fruits.insert(1,"Gauva")
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits) 

# Q3. Take a list [10, 20, 30, 40, 50]. 
# Remove the element 30 and also remove the last element, then print the list.
num=[10,20,30,40,50]
num.remove(30) # it means it remove direct elemnet
print(num)
num.pop(-1) # it remove element by index value
print(num)
# Q4. Take a list [5, 2, 9, 1, 7]. Print it sorted in ascending order and 
# then in descending order.
num=[5,2,9,1,7]
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(sorted(num))

# Q5. Take a list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Using slicing,
# print the first 3 elements, the last 3 elements, and the elements at index 2 to 6.
num=[1,2,3,4,5,6,7,8,9,10]
first=num[:3]
print(first)
last=num[-3:]
print(last)
middle=num[2:6]
print(middle)

# Q6. Using slicing, print the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] in reverse order,
#  and then print only the even-indexed elements (index 0, 2, 4, ...).
num=[1,2,3,4,5,6,7,8,9,10]
a=num[::-1]
print(a)
b=num[0:10:2]
print(b)

# Q7. Take a list [4, 8, 15, 16, 23, 42] 
# and print the largest element, the smallest element, and the sum of all elements.

a=[4,8,15,16,23,42]
b=max(a)
print(b)
c=min(a)
print(c)
print(sum(a))

# Q8. Take 5 numbers from the user, one by one, using input(), store them in a list, 
# and print the list.
# a=int(input("Enter 1st Number:"))
# b=int(input("Enter 2nd Number:"))
# c=int(input("Enter 3rd Number:"))
# d=int(input("Enter 4th Number:"))
# e=int(input("Enter 5th Number:"))
# l=[a,b,c,d,e]
# print(l)

#Q9 WAP to ask the user to enter the name of their 3 fav movie and store them in a list.
# user1=input("Enter your fav movie:")
# user2=input("Enter your fav movie:")
# user3=input("Enter your fav movie:")
# li=[user1,user2,user3]
# print(li)

# WAP to check if a list contains palindrome of element.
a=[1,2,3,2,1]
b=a.copy()
b.reverse() 
print(a==b)

c=[1,"abc",1,"abc"]
d=c.copy()
d.reverse()
print(c==d)

# WAP to count the number of the student with the "A" grade following the tuple.
tup=("C",'D','A','A','B','B','A')
print(tup.count("A"))

# WAP a program to store ("C",'D','A','A','B','B','A') in a list A to D.
li=['C','D','A','A','B','B','A']
li.sort()
print(li)

# Create a list of your 5 favourite programming languages. Print the first and the
# last one using both positive and negative indexing.
PL=['python','sql','java','javascript','php']
first=PL[0]
last=PL[-1]
print(f"The first language is {first} and second language is {last} ")

# Slice the Marks
# Given marks = [45, 67, 89, 23, 90, 56, 78] :
# Print the first 3 marks
# Print the last 2 marks
# Print every alternate mark
# Print the list in reverse

Given_marks=[45,67,89,23,90,56,78]
f3_marks=Given_marks[0:3]
l2_marks=Given_marks[-2:]
Alt_marks=Given_marks[0::2]
rev_marks=Given_marks[::-1]
print(f"{f3_marks}\n{l2_marks}\n{Alt_marks}\n{rev_marks}")
