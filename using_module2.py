#using queue module for stack implementation.
#the queue model has LifoQueue class. For insertion and deletion of elements in this model we use put() and get() functions.
import queue
stack = queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
stack.get()
