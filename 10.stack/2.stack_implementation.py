# implementation using linked list ( interview purpose)
## implementation steps
# 1. create a "top" pointer that will move with new node everytime
# 2. As soon as we create new node, assign its next pointer = last top
# 3. now assign to new top = new node, that is all.
##  basically here we point pointers to previous nodes everytime we move so that when we delete a node ,
##  top can be popped and go beck to second last value

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None  # Initialize an empty stack
    
    def is_empty(self):
        return self.top is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        else:
            popped = self.top.data
            self.top = self.top.next
            return popped
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        else:
            return self.top.data
    
    def size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    

# Create a new stack instance
stack = Stack()

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Print the stack size
print("Stack size:", stack.size())

# Peek at the top element
print("Top element (peek):", stack.peek())

# Pop elements from the stack
print("Pop elements:")
while not stack.is_empty():
    print(stack.pop())

# Try to pop from an empty stack (will raise IndexError)
# stack.pop()
