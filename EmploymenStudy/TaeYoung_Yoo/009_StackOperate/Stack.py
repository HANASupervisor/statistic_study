# # 스택 기본 알고리즘
# class Stack():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.items = [None] * capacity
#         self.top = -1
#
#     def IsFull(self):
#         return self.top == self.capacity - 1
#
#     def IsEmpty(self):
#         return self.top == -1
#
#     def push(self, item):
#         if self.IsFull():
#             raise IndexError('List out of range')
#         self.top += 1
#         self.items[self.top] = item
#
#     def pop(self):
#         if self.IsEmpty():
#             raise IndexError('List out of range')
#         item = self.items[self.top]
#         self.items[self.top] = None
#         self.top -= 1
#         return item
#
#     def peek(self):
#         if self.IsEmpty():
#             raise IndexError('데이터 부족')
#         return self.items[self.top]
#
#
#
# stacking = Stack(10)
# stacking.push(10)
# stacking.push(20)
# stacking.push(30)
#
# print(stacking.peek())
# print(stacking.pop())
# print(stacking.pop())
# print(stacking.pop())
# print(stacking.IsEmpty())
# print(stacking.IsFull())

# 괄호검사
def check_match(character):
    # 괄호를 이용해서 문제풀건데 스택을 활용한다.
    # 만약 왼쪽 괄호가 오면 스택에 집어넣고
    # 오른쪽 괄호가 오면 스택에서 하나씩 꺼내서 비교한다.
    # 만약 비교해서 매치가 안되면 0반환 매치되면 1반ㄴ환
    # 다 매치가 끝났는데 스택에 괄호가 남아있거나 닫는괄호가 남아있는경우 0
    stack_list =[]

    match_dict = {')':'(', '}':'{', ']':'['}
    for chr in character:
        if chr in ('(', '{', '['):
            stack_list.append(chr)

        # 만약 닫는 괄호가 나오면 팝해서 뺀값이랑 같은지 확인하고
        # 같으면 반환
        elif chr in (')', '}', ']'):
            if not stack_list:
                return False

            if match_dict[chr] != stack_list.pop():
                return False

    return len(stack_list) == 0


examples = ['(a(b)', 'a(b)c)', 'a{b(c[d]e}f)']
for ex in examples:
    exa = list(ex)
    print(check_match(exa))
    # if check_match(ex):
    #     print(f'{ex}는 올바른 괄호')
    # else:
    #     print(f'{ex}는 올바르지 않은 괄호')



# greedy
# 모자 뒤로 돌리기




