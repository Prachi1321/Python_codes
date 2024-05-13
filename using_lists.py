#implementation of stacks using using lists:
stack=[]
def push():
    element=int(input("enter the element: "))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("the stack is empty")

    else:
        e=stack.pop()
        print("removed element",e)
        print(stack)
while True:
    choice=int(input("Enter the choice: 1.Push, 2.Pop, 3.Quit"))
    if choice==1:
        push()
    if choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter the correct operation")