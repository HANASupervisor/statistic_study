# 0.05697s
def SecureTheView(arr, N):
    # 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에 있는 건물은 항상 높이가 0이다. (예시에서 빨간색 땅 부분)
    view = 0
    for index in range(2,N-2):
        if arr[index]> arr[index-2] and arr[index]> arr[index-1] and arr[index]> arr[index+1] and arr[index] > arr[index+2]:
            while arr[index]> arr[index-2] and arr[index]> arr[index-1] and arr[index]> arr[index+1] and arr[index] > arr[index+2]:
                # 조망권 확보된 칸 하나 늘리고
                view += 1
                # 자기 칸을 한칸 줄여서 다시비교
                arr[index] -= 1

    return view
 
T = 10
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{test_case} {SecureTheView(arr, N)}')