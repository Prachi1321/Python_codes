# Python program to print all odd numbers in a range
def print_odd(start,end):
    a=[]
    for i in range(start,end+1):
        if i%2!=0:
            a.append(i)
    print(a)
print_odd(4,15)
