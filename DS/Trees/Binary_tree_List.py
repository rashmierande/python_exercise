#Implement Binary tree using lists

def BinaryTree(r):
    return[r,[],[]]

#Insert Left child
def insertLeft(root,newBranch):
    t = root.pop(1)
    #if it has something
    if len(t) >1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])

    return root

#Insert Right child
def insertRight(root,newBranch):
    t = root.pop(2)
    #if it has something
    if len(t) >1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])

    return root

#Get root value
def getRootVal(root):
    return root[0]

#Set a new root value
def setRootVal(root,newVal):
    root[0]=newVal

#Get left child
def getLeftChild(root):
    return root[1]

#Get right child
def getRightChild(root):
    return root[2]

r  = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)

l = getLeftChild(r)
print(r)
print(l)
print(getRightChild(r))
print(getRootVal(r))