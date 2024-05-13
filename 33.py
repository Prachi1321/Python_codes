# Python – List product excluding duplicates
# The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
# Duplication removal list product : 90
list = [1, 3, 5, 6, 3, 5, 6, 1]
str(list)
res=[]
count=0
mul=1
for i in list:
    if list.count(i)>1:
        if i not in res:
            count+=1
            res.append(i)
            
            mul=mul*i
print(res)
print(mul)