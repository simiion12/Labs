from abc import ABC, abstractmethod
from collections import deque


class Queue(ABC):
    @abstractmethod
    def enqueue(self, item):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass


class ListQueue(Queue):
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise Exception("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise Exception("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


class TwoStackQueue(Queue):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.is_empty():
            if not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            raise Exception("Queue is empty")

    def peek(self):
        if not self.is_empty():
            if not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
        else:
            raise Exception("Queue is empty")

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)


list_queue = ListQueue()

list_queue.enqueue("apple")
list_queue.enqueue("banana")
list_queue.enqueue("cherry")

print("Is the ListQueue empty?", list_queue.is_empty())  # False
print("Front element of ListQueue:", list_queue.peek())  # "apple"

print("Dequeued element from ListQueue:", list_queue.dequeue())  # "apple"
print("Dequeued element from ListQueue:", list_queue.dequeue())  # "banana"
print("Dequeued element from ListQueue:", list_queue.dequeue())  # "cherry"

print("Is the ListQueue empty?", list_queue.is_empty())  # True


two_stack_queue = TwoStackQueue()

two_stack_queue.enqueue("apple")
two_stack_queue.enqueue("banana")
two_stack_queue.enqueue("cherry")

print("Is the TwoStackQueue empty?", two_stack_queue.is_empty())  # False
print("Front element of TwoStackQueue:", two_stack_queue.peek())  # "apple"

print("Dequeued element from TwoStackQueue:", two_stack_queue.dequeue())  # "apple"
print("Dequeued element from TwoStackQueue:", two_stack_queue.dequeue())  # "banana"
print("Dequeued element from TwoStackQueue:", two_stack_queue.dequeue())  # "cherry"

print("Is the TwoStackQueue empty?", two_stack_queue.is_empty())  # True
