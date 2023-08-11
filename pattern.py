n=int(input("Enter"))
for i in range(1, n+1):
    for j in range(1, i):
        print(2**i, end=' ')
    print('\r')


    