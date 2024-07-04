# linked lists use nodes that contain data and a reference (or pointer) to the next node in the sequence.
# non-continuos memory allocation

# advantange -> Dynamic Size
# disadvantage -> No random access, Extra Memory to store pointers

# Application

##- stack and queue implementation: linked lists use nodes that contain data and a reference (or pointer) to the next node in the sequence.
##- Dynamic Memory Allocation: Linked lists allow efficient allocation and deallocation of memory at runtime
##- Hash Tables: Linked lists are used in separate chaining to handle collisions in hash tables.

# use case
## 1. media player ( single, double)
## 2. Undo Functionality in Text Editors( doubly)
## 3. Navigation Systems in Web Browsers
## 4. Job Scheduling in Operating Systems

## implementation trick
# 1. make a class Node to create a node with a value and null pointer
# 2. make a class linked_list to do operations on that node
# 3. create a head first in liked_list class that will be create when we initilize libkedlist 
# 3. call node class to create node from linked_list class at runtime

# Operations
# 1. create a linkedlist
# 2. append
# 3. search
# 4. print
# 5. count
# 6. prepand
# 7. insert
# 8. delete


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
        
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_node(self, key):
        current = self.head
        
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if current is None:
            return
        
        prev.next = current.next
        current = None
    
    def delete_at_position(self, position):
        if self.head is None:
            return
        
        current = self.head
        
        if position == 0:
            self.head = current.next
            current = None
            return
        
        prev = None
        count = 0
        while current and count != position:
            prev = current
            current = current.next
            count += 1
        
        if current is None:
            return
        
        prev.next = current.next
        current = None
    
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False


# Example usage:
if __name__ == "__main__":
    # Create a new linked list
    llist = LinkedList()
    
    # Append some elements
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    
    # Print the initial list
    print("Initial linked list:")
    llist.print_list()
    
    # Insert "X" at the beginning
    llist.prepend("X")
    print("\nAfter prepend 'X':")
    llist.print_list()
    
    # Insert "Y" after "B"
    node_b = llist.head.next  # Assuming "B" is the second element
    llist.insert_after_node(node_b, "Y")
    print("\nAfter inserting 'Y' after 'B':")
    llist.print_list()
    
    # Delete "C" from the list
    llist.delete_node("C")
    print("\nAfter deleting 'C':")
    llist.print_list()
    
    # Delete node at position 1 (assuming 0-indexed)
    llist.delete_at_position(1)
    print("\nAfter deleting node at position 1:")
    llist.print_list()
    
    # Search for "B" in the list
    key = "B"
    if llist.search(key):
        print(f"\n'{key}' found in the list.")
    else:
        print(f"\n'{key}' not found in the list.")






