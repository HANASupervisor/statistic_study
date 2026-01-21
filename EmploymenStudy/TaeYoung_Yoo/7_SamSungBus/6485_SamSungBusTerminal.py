def SamSungBus(N, bus, P, bus_terminal):
    # 빈배열을 만든다.
    blank_list = [0] * 5001
    #버스가 지나가는 정류장 번호를 모두 담는 리스트를 만든다
    bus_list = []
    # 버스 노선도 따라가면서 정류장번호를 bus_list에 담는다.
    for idx in range(len(bus)):
        for num in range(bus[idx][0], bus[idx][1]+1):
            bus_list.append(num)

    # 이러면 버스정류장마다 각각 몇번 지나가는지 넣어주면 끝남
    for bus_st in bus_list:
        blank_list[bus_st] += 1

    return ' '.join(str(blank_list[x]) for x in bus_terminal)


T = int(input())
for testCase in range(1, T+1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_terminal = [int(input()) for _ in range(P)]

    print(f'#{testCase} {SamSungBus(N, bus, P, bus_terminal)}')


# 1
# 2
# 1 3
# 2 5
# 5
# 1
# 2
# 3
# 4
# 5


