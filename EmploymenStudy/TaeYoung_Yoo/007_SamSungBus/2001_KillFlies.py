def KillFlies(arr, N, M):
    dr = [0, 0, 1, 1]
    dc = [0, 1, 0, 1]
    max_sum = 0
    for row in range(N - M + 1):
        for col in range(N - M + 1):
            summation = 0
            for idx in range(M):
                for jdx in range(M):
                    nrow = row + idx
                    ncol = col + jdx
                    summation += arr[nrow][ncol]

            if summation > max_sum:
                max_sum = summation
    return max_sum



T = int(input())
for test_case in range(T):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{test_case+1} {KillFlies(arr, N, M)}')


# 2
# 5 2
# 1 3 3 6 7
# 8 13 9 12 8
# 4 16 11 12 6
# 2 4 1 23 2
# 9 13 4 7 3
# 6 3
# 29 21 26 9 5 8
# 21 19 8 0 21 19
# 9 24 2 11 4 24
# 19 29 1 0 21 19
# 10 29 6 18 4 3
# 29 11 15 3 3 29