# implementing using collections model 
#collections model has a class know as deque() which menas double ended queue that helps in the insertion and deletion 
#of elements from both the sides, but here we are implementing a stack which follows LIFO model which means last 
#in first out.
import collections
stacks=collections.deque()
stacks.append(10)
stacks.append(20)
stacks.append(30)
print(stacks)
stacks.pop()
print(stacks)
