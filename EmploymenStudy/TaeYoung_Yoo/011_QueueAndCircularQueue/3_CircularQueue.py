class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.items = [None] * self.capacity # 원형큐는 순환이 핵심 빈것과 가득찬것을 구분하기위해 첫번째 칸은 반드시 비운다.
        self.front = 0 # 앞부분
        self.rear = 0 # 끝부분

    # 큐가 가득찼다는 말은 rear에서 1만큼의 인덱스를 더한 값이 front와 같다는 의미
    def Is_Full(self):
        return (self.rear + 1) % self.capacity == self.front

    # 큐가 비어있다면 데이터 집어넣을수 있다.
    def Enqueue(self, item):
        if self.Is_Full():
            raise IndexError('Queue is full')
        self.rear += 1
        self.items[self.rear % self.capacity] = item

    # 큐가 비어있다는 것은 rear와 front가 같다는 의미
    def Is_Empty(self):
        return self.front == self.rear

    # 큐에 데이터가 들어있다면 비우는 기능 역시 만들수있다.
    def Dequeue(self):
        if self.Is_Empty():
            raise IndexError('Queue is Empty')
        self.front += 1
        item = self.items[self.front % self.capacity]
        self.items[self.front % self.capacity] = None
        return item

    # 큐에 데이터가 뭐가 들어있는지 조회할 수도 있다.
    def peek(self):
        if self.Is_Empty():
            raise IndexError('Queue is Empty')
        return self.items[(self.front + 1) % self.capacity]