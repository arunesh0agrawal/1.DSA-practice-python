# implementaion ( linked list for interview purpose)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Create a queue and perform some operations
queue = Queue()

# Enqueue elements
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

# Display the queue
print("Queue after enqueuing 10, 20, 30, 40:")
queue.display()

# Dequeue elements
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())

# Display the queue
print("Queue after dequeuing two elements:")
queue.display()

# Peek at the front element
print("Front element is:", queue.peek())

