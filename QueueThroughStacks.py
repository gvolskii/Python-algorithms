class Queue:
    
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, item):
        self.stack_1.push(item)

    def dequeue(self):
        if self.stack_2.size():
            return self.stack_2.pop()
        while self.stack_1.size():
            self.stack_2.push(self.stack_1.pop())
        return self.stack_2.pop()
            
    def size(self):
        return self.stack_1.size() + self.stack_2.size()
