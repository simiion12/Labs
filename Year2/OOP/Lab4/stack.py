class StackQueue:
    def push(self, element):
        pass

    def pop(self):
        pass

    def element(self):
        pass

    def is_empty(self):
        pass

class ArrayUpStack(StackQueue):
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, element):
        if len(self.stack) < self.size:
            self.stack.append(element)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")

    def element(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise Exception("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack(StackQueue):
    def __init__(self):
        self.top = None

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            top_data = self.top.data
            self.top = self.top.next
            return top_data
        else:
            raise Exception("Stack is empty")

    def element(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise Exception("Stack is empty")

    def is_empty(self):
        return self.top is None

class ListStack(StackQueue):
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")

    def element(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise Exception("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

# Create an instance of ArrayUpStack with a size of 5
array_stack = ArrayUpStack(5)

# Push elements onto the stack
array_stack.push(1)
array_stack.push(2)
array_stack.push(3)

# Check if the stack is empty
print("Is the ArrayUpStack empty?", array_stack.is_empty())  # False

# Check the top element
print("Top element of ArrayUpStack:", array_stack.element())  # 3

# Pop elements from the stack
print("Popped element from ArrayUpStack:", array_stack.pop())  # 3
print("Popped element from ArrayUpStack:", array_stack.pop())  # 2
print("Popped element from ArrayUpStack:", array_stack.pop())  # 1

# Check if the stack is empty again
print("Is the ArrayUpStack empty?", array_stack.is_empty())  # True

# Create an instance of LinkedStack
linked_stack = LinkedStack()

# Push elements onto the stack
linked_stack.push("apple")
linked_stack.push("banana")
linked_stack.push("cherry")

# Check if the stack is empty
print("Is the LinkedStack empty?", linked_stack.is_empty())  # False

# Check the top element
print("Top element of LinkedStack:", linked_stack.element())  # "cherry"

# Pop elements from the stack
print("Popped element from LinkedStack:", linked_stack.pop())  # "cherry"
print("Popped element from LinkedStack:", linked_stack.pop())  # "banana"
print("Popped element from LinkedStack:", linked_stack.pop())  # "apple"

# Check if the stack is empty again
print("Is the LinkedStack empty?", linked_stack.is_empty())  # True

# Create an instance of ListStack
list_stack = ListStack()

# Push elements onto the stack
list_stack.push("dog")
list_stack.push("cat")
list_stack.push("bird")

# Check if the stack is empty
print("Is the ListStack empty?", list_stack.is_empty())  # False

# Check the top element
print("Top element of ListStack:", list_stack.element())  # "bird"

# Pop elements from the stack
print("Popped element from ListStack:", list_stack.pop())  # "bird"
print("Popped element from ListStack:", list_stack.pop())  # "cat"
print("Popped element from ListStack:", list_stack.pop())  # "dog"

# Check if the stack is empty again
print("Is the ListStack empty?", list_stack.is_empty())  # True
