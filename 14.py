# Python – List product excluding duplicates
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
res=[]
mul=1
for i in range(len(test_list)):
    if test_list.count(i)>1:
        res.append(i)
for j in res:
    mul=mul*j
print(mul)
    


