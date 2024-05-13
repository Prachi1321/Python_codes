# Python – Swap elements in String list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
res=str(test_list)
res= res.replace('G','_').replace("e","G").replace('_','e')
print(res)