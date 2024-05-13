# Python – Extract words starting with K in String List
# Input : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I love G4G”], K = l 
# Output : [‘learning’, ‘love’] 
test_list = ["Gfg is best", "Gfg is for geeks", "I love G4G"]
 
# printing original list
# print("The original list is : " + str(test_list))
 
# initializing K
K=input("enter: ")
 
t = []
for i in test_list:
    # splitting phrases
    temp = i.split()
    for ele in temp:
 
        # checking for matching elements
        if ele[0].lower() == K.lower():
            t.append(ele)
 
# printing result
print("output " + str(t))