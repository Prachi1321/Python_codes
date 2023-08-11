# Input : tuples = [(), (‘ram’,’15’,’8′), (), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”,”),()]
# Output : [(‘ram’, ’15’, ‘8’), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”, ”)]
tuples = [(), ('0', '00', '000'), ('birbal', "" , '45'), (""), (),  (","),()]
for i in tuples:
    if i==():
        tuples.remove(i)
print(tuples)