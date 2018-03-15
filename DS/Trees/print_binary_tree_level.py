import collections

class Node:

    def __init__(self,val = None):
        self.val = val
        self.left = None
        self.right = None

def levelOrderPrin(tree):
    if not tree:
        return
    nodes = collections.deque([tree])
    currentCount, nextCount = 1,0

    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount -=1
        print(currentNode.val,end = " ")
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount +=1
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount +=1
        if currentCount ==0:
            #finished printing current level
            print("\n")
            currentCount, nextCount = nextCount,currentCount



root = Node(1)
root.left =Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


levelOrderPrin(root)