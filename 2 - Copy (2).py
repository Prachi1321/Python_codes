# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]
list = [23, 65, 19, 90]
list[0],list[2]=list[2],list[0]
print(list)