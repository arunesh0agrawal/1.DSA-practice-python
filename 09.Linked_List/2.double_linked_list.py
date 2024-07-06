# each node contains data and two pointers or references: one to the next node in the sequence and another to the previous node. 
# traversal in both directions (forward and backward)

class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLL:

    def __init__(self):
        self.head = None

    def print(self):
        current = self.head
        # Both way are correct
        while current.next:
            print(current.data, end="->" )
            current = current.next
        print(current.data)

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return "found"
            current = current.next
        return "not found"
    
    def count(self):
        count = 0
        current = self.head
        while current:
            count = count + 1
            current = current.next
        return count
    
    def prepand(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        new_node.prev = self.head
        self.head = new_node


    def delete(self):
        #implement during revision time
        pass

    def insert_after_a_value(self, value, data):
        
        current = self.head
        if not current:
            return "list is empty"
        new_node = Node(data)
        
        while current.data != value:
            current = current.next
            if not current:
                return "no such node is available"

        current.next.prev = new_node   
        new_node.next = current.next
        current.next = new_node
        new_node.prev = current
        return 
    
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

DLL = DoubleLL()
DLL.append("A")
DLL.append("B")
DLL.prepand("C")
print(DLL.insert_after_a_value("A", "E"))
DLL.print()
print(DLL.count())
print(DLL.search("A"))
