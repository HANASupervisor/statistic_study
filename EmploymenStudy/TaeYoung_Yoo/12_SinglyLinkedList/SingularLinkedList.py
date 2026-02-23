# 지금까지 했던 자료구조 복습하면서 링크드 리스트 진행해보자
# class Stack:
#     def __init__(self, capacity):
#         self.top = -1
#         self.capacity = capacity
#         self.items = [None] * capacity
#
#     def IsFull(self):
#         return self.top == self.capacity -1
#
#     def append(self, item):
#         if self.IsFull():
#             raise IndexError('Stack is full')
#         self.top += 1
#         self.items[self.top] = item
#
#     def IsEmpty(self):
#         return self.top == -1
#
#     def delete(self):
#         if self.IsEmpty():
#             raise IndexError('Stack is Empty')
#         # 아이템 반환할거 저장하고
#         item = self.items[self.top]
#         # 아이템 지우고
#         self.items[self.top] = None
#         # top한칸 전으로 옮기고
#         self.top -= 1
#         return item
#
#     def peek(self):
#         if self.IsEmpty():
#             raise IndexError('Stack is Empty')
#         return self.items[self.top]
#
# stack = Stack(10)
# stack.append(1)
# stack.append(2)
# print(stack.peek())
# stack.append(3)
#
# print(stack.delete())
# print(stack.delete())
# print(stack.delete())


# 이번에는 큐
# class Queue:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.rear = -1
#         self.front = -1
#         self.items = [None] * capacity
#
#     def IsFull(self):
#         return self.rear == self.capacity - 1
#
#     # Enqueue
#     def enqueue(self, item):
#         if self.IsFull():
#             raise IndexError('Queue is full')
#         self.rear += 1
#         self.items[self.rear] = item
#
#     # 이제 지워야지
#     def IsEmpty(self):
#         return self.front == self.rear
#
#     def dequeue(self):
#         if self.IsEmpty():
#             raise IndexError('Queue is Empty')
#         self.front += 1
#         item = self.items[self.front]
#         self.items[self.front] = None
#         return item
#
#     def peek(self):
#         if self.IsEmpty():
#             raise IndexError('Queue is Empty')
#         return self.items[self.front + 1]
#
#
#
# queue = Queue(10)
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
#
# print(queue.dequeue())
# print(queue.peek())
# print(queue.dequeue())
# print(queue.dequeue())

# class CircularQueue:
#     def __init__(self, capacity):
#         self.capacity = capacity + 1
#         self.rear = 0
#         self.front = 0
#         self.items = [None] * self.capacity
#
#     def IsFull(self):
#         return (self.rear + 1) % self.capacity == self.front
#
#     # Enqueue
#     def enqueue(self, item):
#         if self.IsFull():
#             raise IndexError('Queue is full')
#         self.rear += 1
#         self.items[self.rear % self.capacity] = item
#
#     # 이제 지워야지
#     def IsEmpty(self):
#         return self.front == self.rear
#
#     def dequeue(self):
#         if self.IsEmpty():
#             raise IndexError('Queue is Empty')
#         self.front += 1
#         item = self.items[self.front % self.capacity]
#         self.items[self.front % self.capacity] = None
#         return item
#
#     def peek(self):
#         if self.IsEmpty():
#             raise IndexError('Queue is Empty')
#         return self.items[(self.front + 1) % self.capacity]
#
#
#
# queue = CircularQueue(2)
# queue.enqueue(1)
# queue.enqueue(2)
#
#
# print(queue.dequeue())
# print(queue.peek())
# print(queue.dequeue())
# queue.enqueue(3)
# print(queue.dequeue())


# 이제 단방향 연결리스트 만들어보겠습니다.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class SingularLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert(self, data, position):
#         # 삽입할 새로운 노드를 만든다.
#         new_node = Node(data)
#         # 처음에 넣는다면 insert하려는 값에서 다음으로 연결해야하는 좌표를 head에 좌표를 넣는다.
#         # 헤드에 값에 new_node를 넣는다.
#         if position == 0:
#             new_node.next = self.head
#             self.head = new_node
#         # 처음이 아닌곳에 넣는다면 일단 순회하면서 넣어야하는 위치까지간다(position -1)
#         # 현재위치를 계속 업데이트하면서 간다.
#         # 업데이트된 위치로 가고나면 현재 노드에 적힌 다음좌표를 삽입할 노드의 다음좌표에 적는다.
#         #그리고 현재 노드에 적힌 다음좌표를 삽입할 노드의 값으로 업데이트한다.
#         else:
#             current_node = self.head
#             for _ in range(position - 1):
#                 if current_node is None:
#                     print('범위를 벗어났음')
#                     return
#                 current_node = current_node.next
#             new_node.next = current_node.next
#             current_node.next = new_node
#
#     def IsEmpty(self):
#         return self.head is None
#
#     def append(self, data):
#         # 새로운 노드를 만든다.
#         new_node = Node(data)
#         if self.IsEmpty():
#             self.head = new_node
#         else:
#             current = self.head
#             # 링크드 리스트를 계속 업데이트하면서 끝까지 순회한다.
#             # 만약 current.next가 None이면 해당 자리에 new_node로 연결하고 끝
#             while current.next:
#                 current = current.next
#             current.next = new_node
#
#
#     def delete(self, position):
#         if self.IsEmpty():
#             print('비어있습니다.')
#             return
#         if position == 0:
#             deleted_data = self.head.data
#             # head에서 연결되는 거니까 head None
#             self.head = self.head.next
#         else:
#             # head에 있던거 current에 집어넣기
#             current = self.head
#             for _ in range(position - 1):
#                 if current is None or current.next is None:
#                     print('범위 벗어났습니다.')
#                     return
#                 current = current.next
#             deleted_node = current.next
#             deleted_data = deleted_node.data
#             current.next = current.next.next
#
#         return deleted_data
#
#
#     def search(self, position):
#         if self.IsEmpty():
#             print('비어있습니다.')
#             return
#
#         current = self.head
#         for _ in range(position):
#             if current is None:
#                 print('범위 벗어났습니다.')
#                 return
#             current = current.next
#         return current.data



# 단방향 링크드 리스트 풀코드 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, position):
        next_node = Node(data)
        if position == 0:
            next_node.next = self.head
            self.head = next_node
        else:
            curr_node = self.head
            for _ in range(position-1):
                if curr_node is None:
                    return f'error occur'
                curr_node = curr_node.next
            next_node.next = curr_node.next
            curr_node.next = next_node


    def isEmpty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def delete(self, position):
        if self.isEmpty():
            print('아무것도 없습니다.')
            return
        elif position == 0:
            deleted_data = self.head.data
            self.head = self.head.next
        else:
            curr_node = self.head
            for _ in range(position - 1):
                if curr_node is None or curr_node.next is None:
                    print('범위 벗어남')
                    return
                curr_node = curr_node.next
            deleted_node = curr_node.next
            deleted_data = deleted_node.data
            curr_node.next = curr_node.next.next
        return deleted_data


    def search(self, data):
        if self.isEmpty():
            print('리스트가 비어있습니다.')
            return
        else:
            curr_node = self.head
            number = 1
            while curr_node:
                if curr_node.data == data:
                    return number
                curr_node = curr_node.next
                number += 1

            return f'해당 데이터는 리스트내에 없습니다.'





























