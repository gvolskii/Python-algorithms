class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
    

class Stack:
    
    def __init__(self):
        self.head = None
        self.size = 0
        
    def size(self):
        return self.size
    
    def push(self, val):
        if self.size:
            node = Node(val)
            node.next = self.head
            self.head = node
        else:
            node = Node(val)
            self.head = node
        self.size += 1
        
    def pop(self):
        if self.size:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return value
        else:
            return None
        
    def peek(self):
        if self.size:
            return self.head.value
        else:
            return None
