def IterationTest(arr):
    for idx in range(len(arr)):
        if arr[idx] != arr[len(arr) - 1 - idx]:
            return 0

        if idx >= len(arr)-1-idx:
            return 1


T = int(input())
for test_case in range(1, T+1):
    # strip함수로 양쪽에 빈공간 제거해주는게 키포인트
    arr = list(map(str, input().strip()))

    print(f'#{test_case} {IterationTest(arr)}')
