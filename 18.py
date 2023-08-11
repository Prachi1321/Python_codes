# Python program to find the Strongest Neighbour
# Input: 1 2 2 3 4 5
# Output: 2 2 3 4 5
list=[1,2,2,3,4,5]
list2=[]
for i in range(len(list)-1):
    if list[i]<=list[i+1]:
        list2.append(list[i+1])
print(list2)