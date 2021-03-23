class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []

class SimpleTree:
    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)
        
    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        if self.Root is None or self.Root.Children == []:
            return []
        nodes = [self.Root]
        for node in nodes:
            if node.Children:
                nodes += node.Children
        return nodes

    def FindNodesByValue(self, val):
        all_nodes = self.GetAllNodes()
        return [node for node in all_nodes if node.NodeValue == val]
   
    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
   
    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        all_nodes = self.GetAllNodes()
        leaves_number = 0
        for node in all_nodes:
            if node.Children == []:
                leaves_number += 1
        return leaves_number
