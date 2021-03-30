class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:
    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False 

class BST:
    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        finded_node = BSTFind()
        if self.Root is None:
            return finded_node
        node = self.Root
        while node is not None:
            if node.NodeKey == key:
                finded_node.Node = node
                finded_node.NodeHasKey = True
                return finded_node
            if key < node.NodeKey:
                if node.LeftChild is None:
                    finded_node.Node = node
                    finded_node.ToLeft = True
                    return finded_node
                node = node.LeftChild
            else:
                if node.RightChild is None:
                    finded_node.Node = node
                    return finded_node
                node = node.RightChild

    def AddKeyValue(self, key, val):
        finded_node = FindNodeByKey(key)
        if finded_node.NodeHasKey:
            return False
        if finded_node.ToLeft:
            finded_node.Node.LeftChild = BSTNode(key, val, finded_node.Node)
        else:
            finded_node.Node.RightChild = BSTNode(key, val, finded_node.Node)
  
    def FinMinMax(self, FromNode, FindMax):
        finded_element = BSTNode()
        if FromNode is None:
            return finded_element
        node = FromNode
        if FindMax:
            while node.RightChild is not None:
                node = node.RightChild
            finded_element.Node = node
        else:
            while node.LeftChild is not None:
                node = node.LefttChild
            finded_element.Node = node
        return finded_element

    def DeleteNodeByKey(self, key):
        return False

    def Count(self):
        return 0
