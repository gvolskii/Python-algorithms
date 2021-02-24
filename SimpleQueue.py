class Queue:
    
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() > 0:
            item = self.queue[0]
            self.queue.remove(item)
            return item
        return None 

    def size(self):
        return len(self.queue)
