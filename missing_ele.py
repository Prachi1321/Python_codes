a = [2,8,9,11,12,13]
for i in range(len(a)):
    if a[i+1]-a[i]>1:
        print(i+1)
