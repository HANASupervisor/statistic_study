def RecursiveFactorial(num):
    if num == 1:
        return 1
    # 팩토리얼 수식 n * (n-1)...*1 이거 재귀로 구현
    return num * RecursiveFactorial(num-1)

print(RecursiveFactorial(5))