def CountingContinuousOne(arr, N):
    # 순회돌면서 자기 오른쪽 값을 확인해서 그 값이 1이면
    cnt = 0
    max_cnt = 0
    for idx in range(N):
        # 현재 자신의 값을 확인해서 1이면 개수더함
        if arr[idx] == 1:
            cnt += 1
            # 최대 1연속된 개수보다 자기 개수가 많으면 바로 업데이트 아니면 말아
            if cnt > max_cnt:
                max_cnt = cnt
        # 현재 자신의 값을 확인해서 0이면 연속하는 개수 초기화시킴
        elif arr[idx] == 0:
            cnt = 0

    return max_cnt


T = int(input())
for testCase in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    print(f'#{testCase} {CountingContinuousOne(arr, N)}')


# 3
# 10
# 0011001110
# 10
# 0000100001
# 10
# 0111001111