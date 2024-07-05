class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.top is None:
            raise IndexError("stack is empty")
        else:
            popped = self.top.data
            self.top = self.top.next 
            self.size -= 1
            return popped

stack = Stack() 
stack.push(1)
stack.push(2)
stack.push(3)

# Print the stack size
print(stack.size)

# Pop elements from the stack
print("Pop elements:")
print(stack.pop())