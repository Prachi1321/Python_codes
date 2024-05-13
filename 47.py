# The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
# The character list is : ['g', 'o']
list= ['gfg', 'is', 'best', 'for', 'geeks']
res=[]
l2=[]
char_list=['g','o']

for i in list:
    for j in i:
        if j not in char_list:
            res.append(j)
print(res)



