def StackOperation(postfix_expression):
    # 내가 알고있는 대로 설명해봐
    # 내가알기로 숫자가 나오면 stack에 쌓아
    # 피연산자가 뜨면 스택에서 2개뽑아서 두번째꺼에서 첫번째꺼 피연산
    # 해당하는값 스택에 저장 이짓 반복
    arr = list(map(str, postfix_expression.split()))
    stack_list = []

    for char in arr:
        if char.isnumeric():
            stack_list.append(int(char))
        else:
            val1 = stack_list.pop()
            val2 = stack_list.pop()
            if char == '+':
                result = val2 + val1
                stack_list.append(result)
            elif char == '-':
                result = val2 - val1
                stack_list.append(result)
            elif char == '*':
                result = val2 * val1
                stack_list.append(result)
            elif char == '/':
                result = val2 // val1
                stack_list.append(result)

    return stack_list[0]


postfix_expression = '3 5 2 * + 8 4 / -'
result = StackOperation(postfix_expression)
print(result)
