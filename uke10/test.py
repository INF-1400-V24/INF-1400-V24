from container import Container
from sll import SingleLinkedList
from bst import BinarySearchTree

if __name__ == "__main__":

    sll = SingleLinkedList()
    bst = BinarySearchTree()

    print(isinstance(sll, Container))
    print(isinstance(bst, Container))
    