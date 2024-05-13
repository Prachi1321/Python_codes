def factorial(a):
    factorial=1
    while a>0:
        factorial*=a
        a=a-1
    return factorial
print(factorial(6))
