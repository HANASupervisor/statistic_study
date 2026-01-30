class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    # is_full과 enqueue
    def Is_Full(self):
        return self.rear == self.capacity-1

    def Enqueue(self, item):
        if self.Is_Full():
            raise IndexError('Queue is Full')
        self.rear += 1
        self.items[self.rear] = item

    # is_Empty와 dequeue
    def Is_Empty(self):
        return self.front == self.rear

    def Dequeue(self):
        if self.Is_Empty():
            raise IndexError('Queue is Empty')
        self.front += 1
        item = self.items[self.front]
        self.items[self.front] = None
        return item

    # peek
    def peek(self):
        if self.Is_Empty():
            raise IndexError('Queue is Empty')
        return self.items[self.front + 1]


queue = Queue(10)

queue.Enqueue(1)
queue.Enqueue(2)
queue.Enqueue(3)

print(queue.Dequeue()) # 1
print(queue.peek()) # 2
print(queue.Dequeue()) # 2
print(queue.Dequeue()) # 3

print(queue.Is_Empty())
print(queue.Is_Full())

