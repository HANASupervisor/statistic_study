# // 몫임
# % 나머지임
# 16:32:22 실행이 완료되었습니다. 실행 시간 : 0.05865s
def SimplePrimeFactorization(N):
    # 소인수 개수 2,3,5,7,11 = 5개
    number = 5
    conclusion_list = [0] * number
    while N > 1:
        if N % 2 == 0:
            N = N // 2
            conclusion_list[0] += 1
        elif N % 3 == 0:
            N = N // 3
            conclusion_list[1] += 1
        elif N % 5 == 0:
            N = N // 5
            conclusion_list[2] += 1
        elif N % 7 == 0:
            N = N // 7
            conclusion_list[3] += 1
        elif N % 11 == 0:
            N = N // 11
            conclusion_list[4] += 1
    return ' '.join(str(conclusion_list[idx]) for idx in range(len(conclusion_list)))





T = int(input())
for testCase in range(1, T+1):
    N = int(input())
    print(f'#{testCase} {SimplePrimeFactorization(N)}')

