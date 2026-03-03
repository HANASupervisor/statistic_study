import copy


def BallonPang(N, M, arr):
    summation_score = copy.deepcopy(arr)
    # 풍선이 터지는거 고려해야하니 행렬을 순회해야함
    drow = [0,0,1,-1]
    dcol = [1,-1,0,0]
    for row in range(N):
        for col in range(M):
            for dir in range(4):
                for count in range(1, arr[row][col]+1):
                    nrow = row + drow[dir] * count
                    ncol = col + dcol[dir] * count
                    # 만약 nrow, ncol이 범위 안에 들어가면
                    if 0 <= nrow < N and 0 <= ncol < M:
                        summation_score[row][col] += arr[nrow][ncol]

    max_num = -1
    for row in range(N):
        for col in range(M):
            if max_num < summation_score[row][col]:
                max_num = summation_score[row][col]

    return max_num


T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{test_case} {BallonPang(N,M,arr)}')