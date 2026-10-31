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