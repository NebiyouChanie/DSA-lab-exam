class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.isempty():
            print("stack is empty")
            return
        return self.stack.pop()

    def peek(self):
        if self.isempty():
            print("stack is empty")
            return
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def isempty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)

mystack=Stack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.pop()
mystack.display()
