class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None
        

class LinkedList3:  
    def __init__(self):
        self.dummyNode = Node(None)
        self.dummyNode.next = self.dummyNode
        self.dummyNode.prev = self.dummyNode

    def add_in_tail(self, item):
        item.prev = self.dummyNode.prev
        self.dummyNode.prev.next = item
        self.dummyNode.prev = item
        item.next = self.dummyNode 
        
    
    def print_all_nodes(self):
        node = self.dummyNode.next
        while node != self.dummyNode:
            print(node.value)
            node = node.next

    def delete(self, val, all=False):
        node = self.dummyNode.next
        while node != self.dummyNode:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.prev = self.dummyNode.prev
            self.dummyNode.prev.next = newNode
            self.dummyNode.prev = newNode
            newNode.next = self.dummyNode 
            return
        node = self.dummyNode.next
        while node != self.dummyNode:
            if node == afterNode:
                newNode.prev = node
                newNode.next = node.next
                node.next.prev = newNode
                node.next = newNode
            node = node.next