def BabyGin(arr):
    # 트리플랫이거나 런을 찾는 for문을 돌려서 없애자. 근데 여기서 문제
    # 트리플랫 먼저 없애야함. 1,1,2,3,1,4가 있다고해보자
    # 이거는 트리플랫 런하나로 이루어진 베이비 진이지만 런을 먼저 찾아서 없애면
    # 1,1,4만 남아서 베이비진이 안됨. 그래서 트리플랫 먼저없애야함
    arr.sort()
    counting_card = [0] * (max(arr)+1)

    for idx in range(len(arr)):
        counting_card[arr[idx]] += 1

    # 이제 3인거 뺀다
    for jdx in range(len(counting_card)):
        if counting_card[jdx] >= 3:
            counting_card[jdx] -= 3
            if counting_card[jdx] == 3:
                counting_card[jdx] -= 3

    # 이제 run여부를 확인한다.
    for kdx in range(len(counting_card)-2):
        if counting_card[kdx] == counting_card[kdx+1] == counting_card[kdx+2] >= 1:
            counting_card[kdx] -= 1
            counting_card[kdx + 1] -= 1
            counting_card[kdx + 2] -= 1
            if counting_card[kdx] == counting_card[kdx + 1] == counting_card[kdx + 2] >= 1:
                counting_card[kdx] -= 1
                counting_card[kdx + 1] -= 1
                counting_card[kdx + 2] -= 1

    if sum(counting_card) > 0:
        return 0
    elif sum(counting_card) == 0:
        return 1



T = int(input())
for test_case in range(T):
    arr = list(map(int, input()))

    print(BabyGin(arr))