# Python program to Replace all Characters of a List Except the given character
# Input : test_list = ['G’, ‘F’, ‘G’, ‘I’, ‘S’, ‘B’, ‘E’, ‘S’, ‘T’], repl_chr = ‘*’, ret_chr = ‘G’ 
# Output : [‘G’, ‘*’, ‘G’, ‘*’, ‘*’, ‘*’, ‘*’, ‘*’, ‘*’] 
test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
res=[]
repl_chr = "*"
ret_chr = "G"
for i in test_list:
    if i==ret_chr:
        res.append(i)
    else:
        res.append(repl_chr)
print(res)