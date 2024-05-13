# The original list 1 : [[1, 2], [3, 4], [5, 6]]
# The original list 2 : [[3, 4], [5, 7], [1, 2]]
# The uncommon of two lists is : [[5, 6], [5, 7]]
list_1 = [[1, 2], [3, 4], [5, 6]]
list_2 = [[3, 4], [5, 7], [1, 2]]
uncommon = []
for i in range(len(list_1)):

    if list_1[i] not in list_2:
        uncommon.append(list_1[i])
    elif list_2[i] not in list_1:
        uncommon.append(list_2[i])
print(uncommon)
    


