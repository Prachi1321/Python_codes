# Python – Split Strings on Prefix Occurrence
# Input : test_list = [“geeksforgeeks”, “best”, “geeks”, “and”], pref = “geek” 
# Output : [[‘geeksforgeeks’, ‘best’], [‘geeks’, ‘and’]] 
test_list = ["geeksforgeeks", "best", "geeks", "and"]
print(str(test_list))
pref = "geek"
l2=[]
for i in test_list:
    if i.startswith(pref):
        l2.append([i])
    else:
        l2[-1].append(i)
    
print(l2)
