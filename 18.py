# Python program to count Even and Odd numbers in a List
# Input: list1 = [2, 7, 5, 64, 14]
# Output: Even = 3, odd = 2
list1 = [2, 7, 5, 64, 14]
even_count = 0
odd_count = 0
for i in list1:
    if i%2==0:
        even_count += 1
        
    else:
        odd_count += 1
print(even_count)
print(odd_count)     
