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
        finded_node = self.FindNodeByKey(key)
        if finded_node.NodeHasKey:
            return False
        if finded_node.ToLeft:
            finded_node.Node.LeftChild = BSTNode(key, val, finded_node.Node)
        else:
            finded_node.Node.RightChild = BSTNode(key, val, finded_node.Node)
  
    def FinMinMax(self, FromNode, FindMax):
        finded_element = BSTFind()
        if FromNode is None:
            return finded_element
        node = FromNode
        if FindMax:
            while node.RightChild is not None:
                node = node.RightChild
            finded_element.Node = node
        else:
            while node.LeftChild is not None:
                node = node.LeftChild
            finded_element.Node = node
        return finded_element

    def DeleteNodeByKey(self, key):
        removed_node = self.FindNodeByKey(key)
        if not removed_node.NodeHasKey:
            return False
        if removed_node.Node.LeftChild is None and removed_node.Node.RightChild is None:
            if removed_node.Node.Parent is None:
                self.Root = None
            elif removed_node.Node.Parent.LeftChild == removed_node.Node:
                removed_node.Node.Parent.LeftChild = None
            else:
                removed_node.Node.Parent.RightChild = None
            removed_node.Node.Parent = None
        elif removed_node.Node.RightChild is None:
            if removed_node.Node.Parent is None:
                self.Root = removed_node.Node.LeftChild
                removed_node.Node.LeftChild = None
            else:
                removed_node.Node.LeftChild.Parent = removed_node.Node.Parent
                if removed_node.Node.Parent is not None:
                    if removed_node.Node.Parent.LeftChild == removed_node.Node:
                        removed_node.Node.Parent.LeftChild = removed_node.Node.LeftChild
                    else:
                        removed_node.Node.Parent.RightChild = removed_node.Node.LeftChild
                removed_node.Node.Parent = None
        else:
            insert_node = self.FinMinMax(removed_node.Node.RightChild, False)
            if insert_node.Node.RightChild is None:
                if removed_node.Node.RightChild != insert_node.Node:
                    insert_node.Node.Parent.LeftChild = None
                insert_node.Node.Parent = removed_node.Node.Parent
                if removed_node.Node.Parent is not None:
                    if removed_node.Node.Parent.LeftChild == removed_node.Node:
                        removed_node.Node.Parent.LeftChild = insert_node.Node
                    else:
                        removed_node.Node.Parent.RightChild = insert_node.Node  
                else:
                    self.Root = insert_node.Node
            else:
                insert_node.Node.RightChild.Parent = insert_node.Node.Parent
                insert_node.Node.Parent.LeftChild = insert_node.Node.RightChild
                insert_node.Node.Parent = removed_node.Node.Parent
                if removed_node.Node.Parent is not None:
                    if removed_node.Node.Parent.LeftChild == removed_node.Node:
                        removed_node.Node.Parent.LeftChild = insert_node.Node
                    else:
                        removed_node.Node.Parent.RightChild = insert_node.Node 
                else:
                    self.Root = insert_node.Node
            insert_node.Node.LeftChild = removed_node.Node.LeftChild
            insert_node.Node.LeftChild.Parent = insert_node.Node
            if insert_node.Node != removed_node.Node.RightChild:
                insert_node.Node.RightChild = removed_node.Node.RightChild
                insert_node.Node.RightChild.Parent = insert_node.Node 

    def Count(self):
        if self.Root is None:
            return 0
        left_count = BST(self.Root.LeftChild).Count()
        right_count = BST(self.Root.RightChild).Count()
        return 1 + left_count + right_count
