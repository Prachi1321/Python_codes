# Python program to print all even numbers in a range
# Input: start = 4, end = 15
# Output: 4, 6, 8, 10, 12, 14
def print_even(start, end):
    a=[]
    for i in range(start,end+1):
        if i % 2 == 0:
            a.append(i)
    print(a)

print_even(4,15)