def max_nu(*num):
    max=num[0]
    for i in num:
        if max<i:
            max=i
    return max
print(max_nu(1,2,3))






