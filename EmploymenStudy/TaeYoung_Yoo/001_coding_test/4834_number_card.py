#
# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
#
#
#
# [읿력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
# 다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )
#
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.
def maximum_number_of_card(N, card_number_list):
    '''
    :param N: 카드 숫자
    :param card_number_list: 카드 번호들 리스트
    :return: 가장 많이 나온카드 번호와 몇번나왔는지 정보
    '''
    card_dict = {}
    for card_number in card_number_list:
        if card_number not in card_dict:
            card_dict[card_number] = 1
        elif card_number in card_dict:
            card_dict[card_number] += 1


    maxcount = 0
    for card_number, card_count in card_dict.items():
        if card_dict[card_number] > maxcount:
            maxcount = card_dict[card_number]
            maxnumber = card_number
        elif card_dict[card_number] == maxcount and card_number > maxnumber:
            maxnumber = card_number


    return f"{maxnumber} {maxcount}"



T = int(input())
for test_case in range(T):
    N = int(input())
    card_number_list = list(map(int, input()))
    print(f'#{test_case+1} {maximum_number_of_card(N, card_number_list)}')


# 0.05141s














def number_card(arr, max_val=9):
    temp_list = [0]*(max_val+1) ## 빈리스트 0부터 9까지 숫자의 개수가 들어갈 리스트 생성
    for idx in range(len(arr)):
        temp_list[arr[idx]] += 1 # 빈리스트에 0부터 9까지 각각 몇개씩있는지 입력해준다.
    ## 가장 많이 나온 카드 장수 적기 ##
    max_val = 0
    for j in range(len(temp_list)-1, -1,-1):
        if max_val < temp_list[j]:
            max_val = temp_list[j]
            max_idx = j

    return f"{max_idx} {max_val}"

    #     max_val = max(temp_list[::-1])
    #     max_idx = temp_list.index(max_val)
    #
    # return max_idx, max_val

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input()))

    print(f'#{test_case+1} {number_card(arr)}')





# 0.06050s



# [입력]
# 3
# 5
# 49679
# 5
# 08271
# 10
# 7797946543
#
# [출력]
# #1 9 2
# #2 8 1
# #3 7 3