# Given a list of numbers, write a Python program to count positive and negative numbers in a List. 

# Example:

# Input: list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3
list1 = [2, -7, 5, -64, -14]
count1=0
count2=0
for i in list1:
    if i>0:
        count1=count1+1
    else:
        count2=count2+1
print("Total Positive numbers :", count1,',', "Total negative numbers", count2)

