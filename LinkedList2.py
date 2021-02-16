class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
    
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        finded_elements = list()
        node = self.head
        while node is not None:
            if node.value == val:
                finded_elements.append(node)
            node = node.next
        return finded_elements

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node.prev is not None:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                    
                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev                
                if not all:
                    return
            node = node.next
            
        
    def clean(self):
        self.head, self.tail = None, None

    def len(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                self.head, self.tail = newNode, newNode
                newNode.prev, newNode.next = None, None           
                return
            else: 
                newNode.prev = self.tail
                self.tail.next  = newNode
                self.tail = newNode
                return
        node = self.head
        while node is not None:
            if node == afterNode:
                newNode.next = node.next
                node.next = newNode
                newNode.prev = node
                if newNode.next is not None:
                    newNode.next.prev = newNode
                else:
                    self.tail = newNode
                return
            node = node.next
                
    def add_in_head(self, newNode):
        if self.tail is None:
            self.tail = newNode
        else:
            self.head.prev = newNode
        newNode.next, newNode.prev = self.head, None
        self.head = newNode
