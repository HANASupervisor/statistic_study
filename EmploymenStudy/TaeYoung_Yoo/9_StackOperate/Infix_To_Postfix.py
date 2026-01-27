# 중위표기법을 후위표기법으로 바꾸기
def InfixToPostfix(infix_expression):
    # 순회하면서 값을 봐
    # 피연산자면 바로 postfix 리스트에 더해
    # 열린 괄호는 들어갈때는 순위가 제일 높지만 스택안에서는 순위가 제일 낮아
    # 닫힌 괄호가 나오면 열린괄호가 나올때까지 pop해
    # +, - ,*./ 인 경우는 순위에 해당하는 값을 매겨서 내 점수보다
    # 같거나 높은 경우는 내보내주고 아니면 본인값 append
    # 만약 순회가 다 끝났으면 stack안에 있는거 다 postfix리스트에
    # append하고 postfix 리스트 반환한다.
    stack = []
    postfix = []

    op_dict = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}

    for infix in infix_expression:
        # 들어온 피연산자가 숫자인 경우
        if infix.isnumeric():
            # 숫자로 변경해줌. 숫자로 안바꾸면 연산할때 골때림
            postfix.append(int(infix))
        # 들어온 값이 열린 괄호인 경우 그냥 넣어
        elif infix == "(":
            stack.append(infix)
        # 들어온 값이 닫힌 괄호일 경우 열린괄호가 나올때까지 뽑아
        elif infix == ')':
            top_infix = stack.pop()
            while top_infix != '(':
                postfix.append(top_infix)
                top_infix = stack.pop()
        # 들어온 값이 +, -, *, / 인경우
        else:
            # 스택에 마지막에 쌓인 값과 내 값을 비교해서 내가 더크면
            # 스택에 넣어 아니면 계속 빼
            while stack and op_dict[stack[-1]] >= op_dict[infix]:
                top_infix = stack.pop()
                postfix.append(top_infix)
            stack.append(infix)

    while stack:
        postfix.append(stack.pop())

    return ' '.join(str(chr) for chr in postfix)


infix_expression = "3+(5*2)-8/4"
print(f'후위표기식: {InfixToPostfix(infix_expression)}')

