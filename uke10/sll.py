from container import Container

class SingleLinkedList(Container):

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.first = None

    def add(self, element):
        if self.first == None:
            self.first = SingleLinkedList.Node(element)
        else:
            new_node = SingleLinkedList.Node(element)
            new_node.next = self.first
            self.first = new_node

    def contains(self, element):
        curr = self.first
        while curr != None:
            if curr.data == element:
                return True
            curr = curr.next
        return False
    
    def __str__(self):
        info = "["
        curr = self.first
        while curr != None:
            info += f"{curr.data}, "
            curr = curr.next
        info = info[:-2] + "]"
        return info
    
if __name__ == "__main__":
    ll = SingleLinkedList()
    ll.add(40)
    ll.add(20)
    ll.add(1)
    ll.add(8)
    print(ll)