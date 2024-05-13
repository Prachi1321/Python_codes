# Python | Remove empty tuples from a list
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (","),()]
for i in tuples:
    if len(i)==0:
        tuples.remove(i)
print(tuples)