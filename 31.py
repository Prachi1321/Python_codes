#unique items
list = [1, 2, 2, 5, 8, 4, 4, 8]
l2=[]
count=0
for i in list:
    if i not in l2:
        count=count+1
        l2.append(i)
print(count)