class Node:

    def __init__(self,val = None):
        self.val = val
        self.left = None
        self.right = None

#Its orber n efficiency. Going to do postorder traversal
def trimBST(tree,minVal,maxVal):
    if not tree:
        return

    tree.left =trimBST(tree.left,minVal,maxVal)
    tree.right = trimBST(tree.right,minVal,maxVal)

    if minVal <=tree.val<=maxVal:
        print(tree.val)
        return tree

    if tree.val <minVal:
        return tree.right

    if tree.val>maxVal:
        return tree.left


root = Node(8)
root.left = Node(3)
root.right =Node(10)
root.left.left  =Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)
root.right.right.left = Node(13)

print(trimBST(root,5,13))