#sort an arary
def sort(*a):
    
    for i in a:
        if i+1<i:
            return (i,i+1)
print(sort(3,2,1))