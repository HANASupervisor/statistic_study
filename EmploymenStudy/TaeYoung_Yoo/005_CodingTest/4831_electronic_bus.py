def electronic_bus(K, N, M, arr):
    '''
    :param K: 한번의 충전으로 최대한 이동할수 있는 정류장 수 K
    :param N: 종점까지의 거리
    :param M: 충전기가있는 정류장 개수
    :param arr: 충전기가 설치된 정류장 번호
    :return:최소 몇번 충전해야 도착할수 있는지 출력하는 프로그램
    '''
    # while문 돌건데 종료조건은 도착지에 도착했거나
    # 자기 현재위치 기준으로 K바운더리 안에 충전시설이 없는 경우
    position = 0 # 내 현재 위치
    cango = 0 # 갈수 있음.
    count = 0 # 충전 횟수
    # 내가 도착하면 while문 멈추고 아니면 계속 돌아
    while position + K < N:
        # 내가 현재위치에서 갈수있는 정류장 저장
        go_list = [0]
        # 만약 내 위치에서 K범위 안에 갈수있는 정류장 있으면 감
        while position < arr[cango] <= position + K:
            go_list.append(arr[cango])
            cango += 1
            # 리스트 인덱스 넘어가면 break로 깨라
            if cango == len(arr):
                break

        step = go_list.pop()

        if step == 0:
            return 0
        position = step
        count += 1

    return count



T = int(input())
for test_case in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    print(f'#{test_case} {electronic_bus(K,N,M, arr)}')





