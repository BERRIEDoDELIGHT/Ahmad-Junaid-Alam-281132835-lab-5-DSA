# Task 2

class Queue:
  def __init__(self):
    self.queue = []
    
  def enqueue(self, element):
    self.queue.append(element)

  def dequeue(self):
    if self.isEmpty():
      return "Queue empty"
    return self.queue.pop(0)

  def peek(self):
    if self.isEmpty():
      return "Queue empty"
    return self.queue[0]

  def isEmpty(self):
    return len(self.queue) ==0

  def size(self):
    return len(self.queue)
  

myQueue= Queue()

# def main():
  
#     myQueue.enqueue('A')
#     myQueue.enqueue('B')
#     myQueue.enqueue('C')

#     print(myQueue.peek())

#     print(myQueue.dequeue())
#     print(myQueue.queue)
#     print(myQueue.size())
#     print(myQueue.isEmpty())

# main()