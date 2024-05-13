# craeting a dictionary  rom two lists.
a=[1,2,3,4]
b=['one','two','three','four']
my_dict={}
for i in range(len(a)):
    my_dict[a[i]]=b[i]
print(my_dict)