# Python program to check if the list contains three consecutive common numbers in Python
Input = [4, 5, 5, 5, 3, 8,3,3,4,4,4]

# Output : 5
for i in range(len(Input)-2):
    if Input[i]== Input[i+1] and Input[i+1]==Input[i+2]:

        print(Input[i])
    
        

