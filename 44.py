# Python – Split String of list on K character
# The original list is : ['Gfg is best', 'for Geeks', 'Preparing']
# The extended list after split strings : ['Gfg', 'is', 'best', 'for', 'Geeks', 'Preparing']list is : ['Gfg is best', 'for Geeks', 'Preparing']
test_list = ['Gfg is best', 'for Geeks', 'Preparing']
 

 
K = ' '
 

res = []
for ele in test_list:
    sub = ele.split(K)
    res.extend(sub)
 

print (res)