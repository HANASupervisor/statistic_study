def MaxMinusMin(arr):
    # 최소값을 찾는다.
    min_value = min(arr)
    # 최소값과 같은 인덱스위치를 찾는다
    for idx in range(len(arr)):
        if arr[idx] == min_value:
            min_idx = idx
            break
    # 최대값을 찾는다.
    max_value = max(arr)
    # 최대값과 같은 인덱스 위치를 찾는다.
    for idx in range(len(arr)-1, -1, -1):
        if arr[idx] == max_value:
            max_idx = idx
            break
    # 최대값 인덱스에서 최소값 인덱스 뺀다
    return abs(max_idx - min_idx)

T = int(input())
for testCase in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{testCase+1} {MaxMinusMin(arr)}')