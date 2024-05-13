# The original list is : [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
# The list after pairing is : [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]
list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
print(str(list))
res=[]
for sub in list:
    temp=[]
    for j in range(len(sub)-1):
        temp.append([sub[j],sub[-1]])
    res.append(temp)
print(str(res))
