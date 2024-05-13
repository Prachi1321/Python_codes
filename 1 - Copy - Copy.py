# Given a list, write a Python program to swap first and last element of the list.

# Examples: 

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]
list=[12, 35, 9, 56, 24]
# list[0]=list[4]
# list.pop(4)
# list.insert(4,12)
# print(list)
list[0], list[4]=list[4], list[0]
print(list)
