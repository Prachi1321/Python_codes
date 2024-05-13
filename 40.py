# Python program to get all unique combinations of two Lists
# List_1 = ["a","b"]
# List_2 = [1,2]
# Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]] 
List_1 = ["a","b"]
List_2 = [1,2]
l2=[]
for j in range(len(List_2)):
                    for i in range(len(List_1)):
                            
                    
                        l2.append([(List_2[j],List_1[i])])
                      
print(l2)
