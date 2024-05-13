# Python – Replace Substrings from String List
# The original list 1 is : ['GeeksforGeeks', 'is', 'Best', 'For', 'Geeks', 'And', 'Computer Science']
# The original list 2 is : [['Geeks', 'Gks'], ['And', '&'], ['Computer', 'Comp']]
# The list after replacement : ['GksforGks', 'is', 'Best', 'For', 'Gks', '&', 'Comp Science']
list=['GeeksforGeeks', 'is', 'Best', 'For', 'Geeks', 'And', 'Computer Science']
list_2= [['Geeks', 'Gks'], ['And', '&'], ['Computer', 'Comp']]
a=dict(list_2)
b=[]
for i in list:
    for j in a:
        if j in i:
            
            b.append(i.replace(j,a[j]))
print(b)
