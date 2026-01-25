class Stack():
    def __init__(self, capacity):
        # 저장통 크기 사이즈 설정
        self.capacity = capacity
        # 저장통 만들기
        self.items = [None] * capacity
        # 시작위치 인덱스
        self.top = -1

    def isFull(self):
        # top위치가 저장소보다 하나빼줌 인덱스니까 그래서 같으면 찬거임
        return self.top == self.capacity -1

    def isEmpty(self):
        return self.top == -1

    def push(self, item):
        if self.isFull():
            raise IndexError('Stack overflow')
        self.top += 1
        self.items[self.top] = item



    def pop(self):
        if self.isEmpty():
            raise IndexError('Stack Underflow')
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item



    def peek(self):
        # 값을 출력하는거라 비어있으면 에러를 던져야함
        if self.isEmpty():
            raise IndexError('Stack Underflow')
        item = self.items[self.top]
        return item

# 스택 생성 (용량 3)
s = Stack(3)


# push 테스트
s.push(10)
s.push(20)
s.push(30)


print("peek:", s.peek()) # 기대값: 30


# pop 테스트
print("pop:", s.pop()) # 기대값: 30
print("pop:", s.pop()) # 기대값: 20


print("peek:", s.peek()) # 기대값: 10


# 상태 확인
print("isEmpty:", s.isEmpty()) # 기대값: False
print("isFull:", s.isFull()) # 기대값: False