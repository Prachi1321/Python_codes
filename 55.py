# Python – Count Strings with substring String List
# The original list is : ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
# All strings count with given substring are : 2
list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']

subs = 'Geek'
 

count = 0
for i in list:
    if subs in i:
        count =count+1
 
print(count)