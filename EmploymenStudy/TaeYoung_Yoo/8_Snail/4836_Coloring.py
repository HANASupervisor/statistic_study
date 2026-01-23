def Coloring(N, arr):
    cnt = 0
    red = []
    blue = []
    matrix = [[0] * 10 for _ in range(10)]
    for num in arr:
        if num[-1] == 1:
            red.append(num[0:4])
        elif num[-1] == 2:
            blue.append(num[0:4])

    # 빨간색 순회하면서 그 안에 값들 1로 바꾼다.
    for idx in range(len(red)):
        for row in range(red[idx][0], red[idx][2]+1):
            for col in range(red[idx][1], red[idx][3]+1):
                matrix[row][col] = 1

    for jdx in range(len(blue)):
        for blue_row in range(blue[jdx][0], blue[jdx][2]+1):
            for blue_col in range(blue[jdx][1], blue[jdx][3]+1):
                if matrix[blue_row][blue_col] == 1:
                    cnt += 1

    return cnt

T = int(input())
for testCase in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{testCase} {Coloring(N, arr)}')





