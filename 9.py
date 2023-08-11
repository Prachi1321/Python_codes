# Given the start and end of a range, write a Python program to print all negative numbers in a given range.

#  Examples:

# Input: a = -4, b = 5
# Output: -4, -3, -2, -1
a= int(input("enter"))
b= int(input("Enter"))
for i in range(a,b+1):
    if i<0:
        print (i)