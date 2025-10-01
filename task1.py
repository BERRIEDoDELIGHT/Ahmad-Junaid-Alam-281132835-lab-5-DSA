# Task 1 

class Stack:
    def __init__(self):
        self.stack= []

    
    def Push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return "empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack)==0

    def size(self):
        return len(self.stack)

myStack = Stack()

# def main():
#     myStack.Push('A')
#     myStack.Push('B')
#     myStack.Push('C')

#     print(myStack.peek())

#     print(myStack.pop())
#     print(myStack.stack)
#     print(myStack.size())
#     print(myStack.isEmpty())

# main()