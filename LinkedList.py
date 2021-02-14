class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next
            

    def find(self, val):
        node = self.head        
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None
    

    def find_all(self, val):
        node = self.head
        finded_elements = list()
        
        while node is not None:
            if node.value == val:
                finded_elements.append(node)
            node = node.next
        return finded_elements
    

    def delete(self, val, all=False):
        
        node = self.head
        if node is None:
            return
        if node == self.tail and node.value == val:
            self.head, self.tail = None, None       
        node_next = node.next
        
        while node is not None:
            
            if node.value == val:
                if node.next is None:
                    self.tail = self.head = None
                    return
                else:
                    self.head, node.next = node_next, None
                    node = self.head
                    node_next = node.next 
                if not all:
                    return
                continue 
                
            if node_next is not None and node_next.value == val:
                node.next = node_next.next
                node_next.next = None
                node_next = node.next
                if node_next is None:
                    self.tail = node
                if not all:
                    return
                continue
                
            if node_next is not None:
                node, node_next = node.next, node_next.next
            
            else:
                return
            
            
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
                newNode.next = self.head
                self.head = newNode
                if self.tail is None:
                    self.tail = newNode
                return
        node = self.head
        while node is not None:              
            if node == afterNode:
                newNode.next = node.next
                node.next = newNode
                if newNode.next is None:
                    self.tail = newNode
                return
            node = node.next