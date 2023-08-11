# Given a list of numbers, write a Python program to count Even and Odd numbers in a List.

# Example:

# Input: list1 = [2, 7, 5, 64, 14]
# Output: Even = 3, odd = 2
list1 = [2, 7, 5, 64, 14]
count1=0
count2=0
for i in range(len(list1)):
    if i%2==0:
        count1=count1+1
    else:
        count2=count2+1
print("Even",count1,',',"odd",count2)

        

