#Given a list, write a Python program to swap first and last element of the list.

# Examples: 

# Input : [12;, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

list=[12,35,9,56,24]
# list[0],list[-1]=list[-1],list[0]
# print(list)

a=list.pop(0)
b=list.pop(-1)
list.insert(0,b)
list.append(a)
print(list)