# Remove all the occurrences of an element from a list in Python
# Input1: 1 1 2 3 4 5 1 2 1 
# Output1: 2 3 4 5 2 
# Explanation : The input list is [1, 1, 2, 3, 4, 5, 1, 2] and the item to be removed is 1. 
#                               After removing the item, the output list is [2, 3, 4, 5, 2]
list=[1,1,2,3,4,5,1,2,1]
for i in list:
    if 1 in list:
        list.remove(1)
print(list)