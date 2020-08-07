##binarytruu
##create a node to initialize Binary Search Tree
class Node(object):
    #value that we wish to store in the node
    def __init__(self,value):
        self.value = value
        #define initial left/right nodes to be None
        self.leftChild = None
        self.rightChild = None

    def insert(self,data):
        #if value we enter is NOT greater than or less than root, return False
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        elif self.value < data:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self,data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:

            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()
                

    




class BinaryTree(object):
    #root defines the first value in the Binary Tree
    def __init__(self):
    #passing whatever value and setting as root node of binary tree
        self.root = None
#use insert function and call it RECURSIVELY fro mnode class
    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    #search for a value RECURSIVELY when we do a find
    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False
##RECURSIVE traversal methods for binary tree

##preorder: print data of node, recur on left child and recur on right child
    def preorder(self):
        self.root.preorder()
##first recur on left child, then right child, print data of node
    def postorder(self):
        self.root.postorder()
#recur on left child, print data of node, recur on right child
    def inorder(self):
        self.root.inorder()

bst = BinaryTree()
bst.insert(10)
bst.insert(11)

#(bst.preorder())




##
##    def print_tree(self,traversal_type):
##
##    #ptint EVERY node in tree from left to right
##    #start is node that will update to every single recursive function call
##    #traversal is string prints out to screen and update on every recursive fall, return this!
##    def preorder_print(self,start,traversal):
##        #Root->Left->Right subtree
##        if start:
##            traversal += (str(start.value) + "-")
##            traversal = self.preorder_print(start.left, traversal)
##            traversal = self.preorder_print(start.right, traversal)
##        return traversal
### 1
#/ \
#2 3
#/\ \
#4 5 7
#    \
#    8
##tree = BinaryTree(1)
##tree.root.left = Node(2)
##tree.root.right = Node(3)
##tree.root.left.left = Node(4)
##tree.root.left.right = Node(5)
##tree.root.right.left = Node(6)
##tree.root.right.right = Node(7)
##tree.root.right.right.right = Node(8)

##traverse a binary tree steps:
#see if root is empty, it NOT
#traverse left subtree recursively and right side recursively

