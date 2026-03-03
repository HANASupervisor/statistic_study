best = 0
def dfs(arr, N, row, col, score):
    global best

    # 만약 끝점으로 가던 도중 기존의 최적화 동선상 최소값보다 더 크면 굳이 갈필요 없음
    if score >= best:
        return

    # 만약 끝점에 도착하면 그 점수를 최고점수로 업데이트해준다.
    if row == N - 1 and col == N - 1:
        best = score
        return
    # 행방향으로 한칸씩 움직이면서 해당 칸 점수 더해준다.
    if row + 1 < N:
        dfs(arr, N, row + 1, col, score + arr[row+1][col])
    # 열방향으로 한칸씩 움직이면서 해당 칸 점수 더해준다.
    if col + 1 < N:
        dfs(arr, N, row, col + 1, score + arr[row][col + 1])



def BruteForce(arr, N):
    global best
    # 초기 best 값은 제일 크게 잡는다.
    best = 10 ** 18
    # dfs 탐색해서 가장 작은 best값을 찾는다.
    dfs(arr,N, 0,0,arr[0][0])

    return best


T = int(input())
for testCase in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{testCase} {BruteForce(arr, N)}')