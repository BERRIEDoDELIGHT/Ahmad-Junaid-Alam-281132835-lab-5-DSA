from task1 import Stack

def reverse_str(st):
    stack = Stack()
    new = []
    
    for i in st:
        stack.Push(i)

    while not stack.isEmpty():
        popped = stack.pop()
        new.append(popped)

    print("Original", st)
    print("New reversed", new)
    return new
    


def main2():
    b = ['A','B','C']
    reverse_str(b)

    c= ['N','J','G']
    reverse_str(c)


main2()