# Remove empty List from List
# The original list is : [5, 6, [], 3, [], [], 9]
# List after empty list removal : [5, 6, 3, 9]
list= [5, 6, [], 3, [], [], 9]
for i in list:
    if [] in list:
        list.remove([])
print(list)