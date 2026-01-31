import sys
sys.stdin = open('input.txt', 'r')

op_dict = {')': '(', '}': '{', ']': '[', '>': '<'}

def MatchParentheses(arr):
    # 어떻게 풀거야?
    # 스택쓸거임
    stack_list = []

    for chr in arr:
        # 만약 열린 괄호면 스택에 집어넣는다.
        if chr in op_dict.values():
            stack_list.append(chr)
        # 만약 닫힌 괄호면 스택에서 하나 꺼내서 그거랑 값을 비교한다.
        # 비교해서 같으면 계속하고 다르면 0반 반환한다.
        elif stack_list and chr in op_dict.keys():
            if op_dict[chr] == stack_list.pop():
                continue
            else:
                return 0
        # chr만 남았고 stack_list가 비어있다?
        else:
            return 0

    # 순회가 다 끝났으니까 스택이 비어있어야함.
    if not stack_list:
        return 1
    # 스택이 안비어있으면 0
    else:
        return 0


T = 10
for testCase in range(1, T+1):
    N = int(input())
    arr = list(map(str, input()))

    print(f'#{testCase} {MatchParentheses(arr)}')