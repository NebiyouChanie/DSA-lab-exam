class Queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def enqueue(self,data):
        self.stack1.append(data)
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        dequeued=self.stack1.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return dequeued
    def peek(self):
        if self.isEmpty():
            print("queue is empty")
            return
        return self.stack1[0]
    def isEmpty(self):
        return len(self.stack1)==0

    def size(self):
        return len(self.stack1)
    def display(self):
        print(self.stack1)

myqueue=Queue()
myqueue.enqueue(5)
myqueue.enqueue(6)
myqueue.enqueue(7)
myqueue.enqueue(8)
myqueue.dequeue()
myqueue.display()
