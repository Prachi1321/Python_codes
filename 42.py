# Python | Reverse All Strings in String List
# The original list is : ['geeks', 'for', 'geeks', 'is', 'best']
list=['geeks', 'for', 'geeks', 'is', 'best']
l2=[]
for i in list:
    a=i[::-1]
    l2.append(a)
print(l2)