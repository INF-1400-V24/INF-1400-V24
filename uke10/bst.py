from container import Container

class BinarySearchTree(Container):

    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
        
        def insert(self, element):
            if element < self.data:
                if not self.left:
                    self.left = BinarySearchTree.Node(element)
                else:
                    self.left.insert(element)
            else:
                if not self.right:
                    self.right = BinarySearchTree.Node(element)
                else:
                    self.right.insert(element)

        def contains(self, element):
            if self.data == element:
                return True
            if self.left and self.left.contains(element):
                return True
            if self.right and self.right.contains(element):
                return True
            return False
        
        def build_string(self, buildlist):
            if self.left != None:
                self.left.build_string(buildlist)
            buildlist.append(self.data)
            if self.right != None:
                self.right.build_string(buildlist)
            return buildlist

    def __init__(self):
        self.root = None

    def add(self, element):
        if self.root == None:
            self.root = BinarySearchTree.Node(element)
        else:
            self.root.insert(element)

    def contains(self, element):
        if self.root == None:
            return False
        return self.root.contains(element)
    
    def __str__(self):
        if self.root == None:
            return "[]"
        return str(self.root.build_string([]))
    

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(7)
    bst.add(2)
    bst.add(19)
    bst.add(4)
    bst.add(-3)
    print(bst)