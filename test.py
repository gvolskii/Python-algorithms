import unittest
from bst import *

class MyTests(unittest.TestCase):
    def setUp(self):
        self.a10 = BSTNode(10, 'a10', None)
        self.a6 = BSTNode(6, 'a6', self.a10)
        self.a13 = BSTNode(13, 'a13', self.a10)
        self.a5 = BSTNode(5, 'a5', self.a6)
        self.a7 = BSTNode(7, 'a7', self.a6)
        self.a12 = BSTNode(12, 'a12', self.a13)
        self.a14 = BSTNode(14, 'a14', self.a13)
        self.a9 = BSTNode(9, 'a9', self.a7)
        self.a11 = BSTNode(11, 'a11', self.a12)
        self.a8 = BSTNode(8, 'a8', self.a9)
        self.a10.LeftChild = self.a6
        self.a10.RightChild = self.a13
        self.a6.LeftChild = self.a5
        self.a6.RightChild = self.a7
        self.a13.LeftChild = self.a12
        self.a13.RightChild = self.a14
        self.a7.RightChild = self.a9
        self.a12.LeftChild = self.a11
        self.a9.LeftChild = self.a8
        self.A = BST(self.a10)
        '''
                           10
                        /       \ 
                       6         13
                      / \       /  \
                     5   7     12  14
                          \   /
                           9 11
                          /
                         8
        '''
        self.b10 = BSTNode(10, 'b10', None)
        self.b11 = BSTNode(11, 'b11', self.b10)
        self.b12 = BSTNode(12, 'b12', self.b11)
        self.b9 = BSTNode(9, 'b9', self.b10)
        self.b8 = BSTNode(8, 'b8', self.b9)
        self.b10.LeftChild = self.b9
        self.b10.RightChild = self.b11
        self.b9.LeftChild = self.b8
        self.b11.RightChild = self.b12
        self.B = BST(self.b10)
        '''
                         10
                      /      \
                     9        11
                    /          \
                   8            12
        '''

        self.C = BST(None) #Empty three
        self.d10 = BSTNode(10, 'd10', None) #Three with one node
        self.D = BST(self.d10)

    def testFindNodeByKey(self):
        self.assertEqual((self.A.FindNodeByKey(10).NodeHasKey,             # key 10 is in the tree
                          self.A.FindNodeByKey(10).Node, 
                          self.A.FindNodeByKey(10).ToLeft),
                        (True, self.a10, False))
        self.assertEqual((self.A.FindNodeByKey(17).NodeHasKey,             
                          self.A.FindNodeByKey(17).Node, 
                          self.A.FindNodeByKey(10).ToLeft),
                        (False, self.a14, False))
        self.assertEqual((self.A.FindNodeByKey(1).NodeHasKey, 
                          self.A.FindNodeByKey(1).Node, 
                          self.A.FindNodeByKey(10).ToLeft == False),
                        (False, self.a5, True))
        
        
    def testAddKeyValue(self):
        self.assertEqual((self.A.Count(), self.A.AddKeyValue(10, 0), self.A.Count()), (10, False, 10)) # key 10 is in the tree
        self.assertEqual((self.A.Count(), 
                          self.A.AddKeyValue(1, 'a1'), 
                          self.A.Count(), 
                          self.A.FindNodeByKey(1).Node.Parent, 
                          self.A.FindNodeByKey(1).Node),
                        ((10, None, 11, self.a5, self.a5.LeftChild)))
        self.assertEqual((self.A.Count(), 
                          self.A.AddKeyValue(17, 'a17'), 
                          self.A.Count(), 
                          self.A.FindNodeByKey(17).Node.Parent, 
                          self.A.FindNodeByKey(17).Node),
                        (11, None, 12, self.a14, self.a14.RightChild))
        self.assertEqual((self.C.Count(), self.C.AddKeyValue(10, 'c10'), self.C.Count(), self.C.FindNodeByKey(10).Node.Parent, 
                        self.C.FindNodeByKey(10).Node.LeftChild, self.C.FindNodeByKey(10).Node.RightChild, self.C.Root),
                        (0, None, 1, None, None, None, self.C.FindNodeByKey(10).Node))
        
    def testFinMinMax(self):
        self.assertEqual((self.A.FinMinMax(self.a10, True).Node, self.A.FinMinMax(self.a10, False).Node),
                        (self.a14, self.a5))
        self.assertEqual((self.A.FinMinMax(self.a13, True).Node, self.A.FinMinMax(self.a13, False).Node),
                        (self.a14, self.a11))
        self.assertEqual((self.A.FinMinMax(self.a8, True).Node, self.A.FinMinMax(self.a8, False).Node), 
                         (self.a8, self.a8))
        self.assertEqual((self.A.FinMinMax(self.a7, True).Node, self.A.FinMinMax(self.a7, False).Node), 
                         (self.a9, self.a7))
        self.assertEqual((self.A.FinMinMax(self.a6, True).Node, self.A.FinMinMax(self.a6, False).Node), 
                         (self.a9, self.a5))
        
        
        
    def testDeleteNodeByKey(self):
        self.assertEqual((self.A.Count(), self.A.DeleteNodeByKey(8), self.A.FindNodeByKey(8).NodeHasKey, 
                          self.a9.RightChild, self.a9.LeftChild, self.A.Count()),
                        (10, None, False, None, None, 9))
        self.assertEqual((self.A.Count(), self.A.DeleteNodeByKey(14), self.A.FindNodeByKey(14).NodeHasKey, 
                          self.a13.LeftChild, self.a13.RightChild, self.A.Count()),
                         (9, None, False, self.a12, None, 8))
        self.assertEqual((self.A.Count(), self.A.DeleteNodeByKey(17), self.A.Count()), 
                        (8, False, 8))
        self.assertEqual((self.A.Count(), self.A.DeleteNodeByKey(10), self.A.FindNodeByKey(10).NodeHasKey, 
                          self.A.Root, self.a11.RightChild, self.a11.LeftChild, 
                          self.a11.Parent, self.A.Count()), 
                        (8, None, False, self.a11, self.a13, self.a6, None, 7))
        self.assertEqual((self.A.Count(), self.A.DeleteNodeByKey(6), self.A.FindNodeByKey(6).NodeHasKey, 
                          self.a7.LeftChild, self.a7.RightChild, self.a7.Parent, self.A.Root.LeftChild, self.A.Count()),
                         (7, None, False, self.a5, self.a9, self.a11, self.a7, 6))
        self.assertEqual((self.D.Count(), self.D.Root, self.D.DeleteNodeByKey(10), self.D.Count(), self.D.Root),
                         (1, self.d10, None, 0, None))
        self.assertEqual((self.B.Count(), self.B.DeleteNodeByKey(9), self.B.Root.LeftChild, self.b8.Parent, self.B.Count(), 
                          self.B.DeleteNodeByKey(11), self.B.Root.RightChild, self.b12.Parent, self.B.Count()),
                          (5, None, self.b8, self.b10, 4,
                           None, self.b12, self.b10, 3))
        
if __name__ == '__main__':
    unittest.main()