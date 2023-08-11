# Python – Extract elements with Frequency greater than K
# test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
# Output : [4, 3] 
test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K=3
list2=[]
for i in range(len(test_list)):
    if test_list.count(i)>K:
        list2.append(i)
print(list2)