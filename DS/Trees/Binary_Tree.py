class BinaryTree(object):

    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):

        if self.leftChild == None:
            #If no node, add node
            self.leftChild = BinaryTree(newNode)
        else:
            # if has existing child, get a node and insert it,
            # pushing existing node down
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = rightChild(newNode)
            t.leftChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def inOrder(self):
        if self.key != None:
            inOrder(self.getLeftChild())
            print("<<<<",self.getRootVal())
            inOrder(self.getRightChild())

r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())

print ("*************************")

#r.inorder()

