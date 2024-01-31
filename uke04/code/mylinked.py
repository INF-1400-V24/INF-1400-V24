
class MyLinkedList:

    class Node:

        def __init__(self, data):
            self.next = None
            self.data = data

        def insert_next(self, new_node):
            self.next = new_node

        def print_elem(self):
            print(self.data)
            if self.next != None:
                self.next.print_elem()

    def __init__(self):
        self.start = None
        self.end = None

    def insert(self, data):
        if self.start == None:
            self.start = MyLinkedList.Node(data)
            self.end = self.start
        else:
            prev_end = self.end
            new_end = MyLinkedList.Node(data)
            prev_end.insert_next(new_end)
            self.end = new_end
        
    def print_all(self):
        if self.start != None:
            self.start.print_elem()

    def contains(self, data):
        curr_node = self.start
        while curr_node != None:
            if curr_node.data == data:
                return True
            curr_node = curr_node.next
        return False
    
    def remove(self, data):
        if not self.contains(data):
            print("Data finnes ikke i lista")
            return False
        if self.start.data == data:
            self.start = self.start.next
        curr_node = self.start
        while curr_node.next != None:
            if curr_node.next.data == data:
                curr_node.next = curr_node.next.next
                return True
            curr_node = curr_node.next

    def __len__(self):
        n_elems = 0
        curr_node = self.start
        while curr_node != None:
            n_elems += 1
            curr_node = curr_node.next
        return n_elems
    
    def __add__(self, other):
        new_list = MyLinkedList()
        curr_node = self.start
        while curr_node != None:
            new_list.insert(curr_node.data)
            curr_node = curr_node.next
        curr_node = other.start
        while curr_node != None:
            new_list.insert(curr_node.data)
            curr_node = curr_node.next
        return new_list

if __name__ == "__main__":
    ll = MyLinkedList()
    ll.insert("a")
    ll.insert("b")
    ll.insert("c")

    ll2 = MyLinkedList()
    ll2.insert("Per")
    ll2.insert("Berit")
    ll2.insert("Jonas")

    samlet = ll2 + ll

    samlet.remove("Per")
    samlet.print_all()