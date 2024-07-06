# import pdb
# pdb.set_trace()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        current = self.head
        # Both way are correct
        while current.next:
            print(current.data, end="->" )
            current = current.next
        print(current.data)
        # while current:
        #     print(current.data, end="->" )
        #     current = current.next
        # print(None)

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
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    

    def delete(self):
        # implement in next practiec for revison
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
            
        new_node.next = current.next
        current.next = new_node
        return        
        


my_list = LinkedList()
my_list.append("A")
my_list.append("B")

print(my_list.search("A"))
print(my_list.insert_after_a_value("B", "C"))
my_list.print()

    
