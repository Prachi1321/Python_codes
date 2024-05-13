list = [4, 5, 6]
print(str(list))
res=[]
for i in range(len(list)):
    res.append([list[i],list[-2]])
print(str(res))