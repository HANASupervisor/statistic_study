def InfixToPostfix(char):
    # 중위 표기법을 후위표기법으로 바꾸는 방법
    # 숫자가 나오면 그냥 출력한다.
    # (가 나오면 무조건 stack에 넣는다.
    # )가 나오면 (가 나올때까지 계속 pop해서 출력한다.
    # +-*/ 의경우 stack의 마지막 번호가
    # 자기보다 숫자가 같거나 더크면 pop해서 출력하고
    # 자기보다 작은 경우 자신을 stack에 append한다.
    # stack에 남은게 있으면 다 pop해서 출력한다.
    op_dict = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(': 0}

    stack_list =[]
    postfix_list = []

    for chr in char:
        if chr.isnumeric():
            postfix_list.append(chr)
        elif chr == '(':
            stack_list.append(chr)
        elif chr == ')':
            top_ele = stack_list.pop()
            while top_ele != '(':
                postfix_list.append(top_ele)
                top_ele = stack_list.pop()

        else:
            while stack_list and op_dict[stack_list[-1]] >= op_dict[chr]:
                postfix_list.append(stack_list.pop())
            stack_list.append(chr)

    while stack_list:
        postfix_list.append(stack_list.pop())

    return ' '.join(postfix_list)

# 후위표기식 활용해서 연산하기
def calculator(expression):
    # 숫자가 나오면 스택에 다 집어넣고
    # 피연산자가 나오면 스택에서 2개 숫자 꺼내서 두번째로 꺼낸거에서
    # 첫번째로 꺼낸거 연산하면됨
    original_list = expression.split()
    stack_list = []
    for element in original_list:
        if element.isnumeric():
            stack_list.append(int(element))
        else:
            val1 = stack_list.pop()
            val2 = stack_list.pop()
            if element == '+':
                result = val2 + val1
            elif element == '-':
                result = val2 - val1
            elif element == '*':
                result = val2 * val1
            elif element == '/':
                result = val2 // val1
            stack_list.append(result)

    return stack_list[0]




infix_expression = "3+(5*2)-8/4"
print(f'후위표기식: {InfixToPostfix(infix_expression)}')
print(f'계산기 결과: {calculator(InfixToPostfix(infix_expression))}')