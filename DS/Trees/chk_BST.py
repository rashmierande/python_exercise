class Node:
    def __init__(self, val=None):
        self.left, self.right, self.val = None, None, val

#Perform a inorder traversal, it should result in sorted order of values
#  if it is BST
def isBST2(tree, lastNode=[NEG_INFINITY]):

    if tree is None:
        return True

    if not isBST2(tree.left, lastNode):
        return False

    if tree.val < lastNode[0]:
        return False

    lastNode[0]=tree.val

return isBST2(tree.right, lastNode)


#Alternative solution
INFINITY = float("infinity")
NEG_INFINITY = float("-infinity")

def isBST(tree, minVal=NEG_INFINITY, maxVal=INFINITY):
    if tree is None:
        return True
    if not minVal <= tree.val <= maxVal:
        return False

    return isBST(tree.left, minVal, tree.val) and isBST(tree.right, tree.val, maxVal)

INFINITY = float("infinity")
NEG_INFINITY = float("-infinity")

def isBST1(root,min=NEG_INFINITY, max = INFINITY):
    if root is None:
        return True
    #If any node lies outside the range then BST constraint has been violated and we return false
    if root.val <= min or root.val >= max:
        retun False
    #Check the left and right subtree to see if they are valid search trees
    return isBST1(root.left,min,root.val) and
           isBST1(root.right,root.val,max)
