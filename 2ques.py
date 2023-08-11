list= ['lets', 'go', 'to', 'aus']
list1=[]
print("The original list is:", list)
for i in list:
    a= i.replace('g','m').replace('l','c').replace('e', 'a')
    list1.append(a)
print(list1)