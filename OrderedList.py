class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        if v1 > v2:
            return 1
        return 0

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            return
        node = self.head
        if self.__ascending:
            while node is not None and self.compare(new_node.value, node.value) > 0:
                node = node.next
            if node is None:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
                return
            if node.prev is None:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                return
            new_node.next = node
            new_node.prev = node.prev
            node.prev.next = new_node
            node.prev = new_node          
        if not self.__ascending:
            while node is not None and self.compare(new_node.value, node.value) < 0:
                node = node.next
            if node is None:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
                return
            if node.prev is None:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                return
            new_node.next = node
            new_node.prev = node.prev
            node.prev.next = new_node
            node.prev = new_node   
            
            
    def find(self, val):
        node = self.head
        if self.__ascending:
            while node is not None and self.compare(val, node.value) >= 0:
                if val == node.value:
                    return node
                node = node.next
        if not self.__ascending:
            while node is not None and self.compare(val, node.value) <= 0:
                if val == node.value:
                    return node
                node = node.next
        return None

    def delete(self, val):
        node = self.head
        if self.__ascending:
            while node is not None and self.compare(val, node.value) >= 0:
                if val == node.value:
                    if node.prev is None:
                        self.head = node.next
                    else:
                        node.prev.next = node.next
                    if node.next is None:
                        self.tail = node.prev
                    else:
                        node.next.prev = node.prev
                    return
                node = node.next
        if not self.__ascending:
            while node is not None and self.compare(val, node.value) <= 0:
                if val == node.value:
                    if node.prev is None:
                        self.head = node.next
                    else:
                        node.prev.next = node.next
                    if node.next is None:
                        self.tail = node.prev
                    else:
                        node.next.prev = node.prev
                    return
                node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = self.tail = None

    def len(self):
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next
        return length

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if len(v1.strip()) < len(v2.strip()):
            return -1
        if len(v1.strip()) > len(v2.strip()):
            return 1
        return 0
