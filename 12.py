# Program to print duplicates from a list of integers
# list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]
list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
count=0
for i in list:
    if list.count(i)>1:
        list.remove(i)
print(list)
