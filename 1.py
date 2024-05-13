def average(*num):
    sum=0
    for i in num:
        
        sum=sum+i
    print(sum/len(num))
average(1,2,3,4,5)