array=[3,6,2,9,5]
list=[]

a = int(input("Enter the number"))
for i in range(len(array)):
    for j in range(i):

        if array[i]+array[j]==a:
            print((array[i], array[j]))





