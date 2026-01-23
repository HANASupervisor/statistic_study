def Snail(N):
    arr = [[0] * N for _ in range(N)]
    number = [num for num in range(1,N*N+1)]
    drow = [0, 1, 0, -1]
    dcol = [1, 0, -1, 0]
    row , col, dist = 0, 0, 0
    for value in number:
        arr[row][col]= value
        nrow = row + drow[dist]
        ncol = col + dcol[dist]
        if not (0 <= nrow < N and 0 <= ncol < N) or arr[nrow][ncol] != 0:
            dist = (dist+1)%4
            nrow = row + drow[dist]
            ncol = col + dcol[dist]

        row, col = nrow, ncol

    return arr

T = int(input())
for testCase in range(1, T+1):
    N = int(input())
    print(Snail(N))