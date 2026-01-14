def TheBiggestDrop(arr, N):
    '''
    :param arr: 각 칸에 얼만큼의 수화물이 쌓여있는가
    :param N: 방의 사이즈 가로길이와 세로길이
    :return: 최대 낙차 값

    전략: 각행렬을 순회할때 자신의 오른쪽 값과 자신의 크기를 비교해서
    자기보다 작을경우 카운트를 하나 늘리고 그렇지않을경우 그냥 둔다.
    '''
    gravity_list = [0] * N
    for index in range(N):
        for jndex in range(index + 1, N):
            # 만약 arr index가 자신 오른쪽 값보다 더 크면 +1을한다
            if arr[index] > arr[jndex]:
                gravity_list[index] += 1

    return max(gravity_list)




T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{test_case} {TheBiggestDrop(arr, N)}')

# input
# 3
# 9
# 7 4 2 0 0 6 0 7 0
# 9
# 7 4 2 0 0 6 7 7 0
# 20
# 52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53
#
# output
# #1 7
# #2 6
# #3 13



# 풀 설명
# 길이가 5짜리인 리스트가 있다고 생각해보자
# 0번 순회할때 자신의 오른쪽 값1,2,3,4 인덱스 값들과 비교한다.
# 1번 순회할때 자신의 오른쪽 값 2,3,4 인덱스값들과 비교한다.
# 2번 순회할때 자신의 오른쪽값 3,4 인덱스값들과 비교한다.
# 이렇게 비교해서 각 순회별로 각 칸의 최대값들이 몇칸 떨어지는지
# 생각할수 있다.
# 그리고 그값들 중에 가장 큰 값이 최대 낙차가 될것이다.

#