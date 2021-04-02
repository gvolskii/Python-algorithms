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


a10 = BSTNode(10, 'a10', None)
a6 = BSTNode(6, 'a6', a10)
a13 = BSTNode(13, 'a13', a10)
a5 = BSTNode(5, 'a5', a6)
a7 = BSTNode(7, 'a7', a6)
a12 = BSTNode(12, 'a12', a13)
a14 = BSTNode(14, 'a14', a13)
a9 = BSTNode(9, 'a9', a7)
a11 = BSTNode(11, 'a11', a12)
a8 = BSTNode(8, 'a8', a9)


a10.LeftChild = a6
a10.RightChild = a13
a6.LeftChild = a5
a6.RightChild = a7
a13.LeftChild = a12
a13.RightChild = a14
a7.RightChild = a9
a12.LeftChild = a11
a9.LeftChild = a8

A = BST(a10)

#Test FindNodeByKey
print((A.FindNodeByKey(10).NodeHasKey == True, A.FindNodeByKey(10).Node == a10, A.FindNodeByKey(10).ToLeft == False))
print((A.FindNodeByKey(17).NodeHasKey == False, A.FindNodeByKey(17).Node == a14, A.FindNodeByKey(10).ToLeft == False))
print((A.FindNodeByKey(1).NodeHasKey == False, A.FindNodeByKey(1).Node == a5, A.FindNodeByKey(1).ToLeft == True))

#Test AddKeyValue
print((A.Count(), A.AddKeyValue(10, 0) == False, A.Count()))
print((A.Count(), 
       A.AddKeyValue(1, 'a1'), 
       A.Count(), 
       A.FindNodeByKey(1).Node.Parent == a5, 
       A.FindNodeByKey(1).Node == a5.LeftChild))
print((A.Count(), 
       A.AddKeyValue(17, 'a17'), 
       A.Count(), 
       A.FindNodeByKey(17).Node.Parent == a14, 
       A.FindNodeByKey(17).Node == a14.RightChild))

#Test FinMinMax
print((A.FinMinMax(a10, True).Node == A.FindNodeByKey(17).Node,
       A.FinMinMax(a10, False).Node == A.FindNodeByKey(1).Node))
print((A.FinMinMax(a13, True).Node == A.FindNodeByKey(17).Node,
       A.FinMinMax(a13, False).Node == a11))
print((A.FinMinMax(a8, True).Node == a8,
       A.FinMinMax(a8, False).Node == a8))

#Test DeleteNodeByKey
print((A.Count(), A.DeleteNodeByKey(17), A.FindNodeByKey(17).NodeHasKey == False, a14.RightChild is None, A.Count()))
print((A.Count(), A.DeleteNodeByKey(1), A.FindNodeByKey(1).NodeHasKey == False, a5.LeftChild is None, A.Count()))
print((A.Count(), A.DeleteNodeByKey(17), A.Count()))
print((A.Count(), A.DeleteNodeByKey(10), A.FindNodeByKey(10).NodeHasKey == False, A.Root == a11,
       a11.RightChild == a13, a11.LeftChild == a6, a11.Parent is None, A.Count()))
