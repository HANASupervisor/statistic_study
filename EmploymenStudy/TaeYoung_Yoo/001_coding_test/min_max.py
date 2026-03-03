# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
#
#
# [입력]
#
# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
#
# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
#
# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )
#
# [출력]
#
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
def difference_max_min(N, list_condition):
    '''
    :param N: 주어진 리스트에 몇개의 원소가 들어있는가
    :param list_condition:  주어진 리스트
    :return: 갑이 얼마만큼 차이가 나는가
    '''
    max_element = 0
    min_element = 1000000
    for element in list_condition:
        if element > max_element:
            max_element = element
        elif element < min_element:
            min_element = element

    return max_element - min_element

def difference_max_min1(N, list_condition):
    '''
    :param N: 주어진 리스트에 몇개의 원소가 들어있는가
    :param list_condition:  주어진 리스트
    :return: 갑이 얼마만큼 차이가 나는가
    '''
    return max(list_condition) - min(list_condition)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    list_condition = list(map(int, input().split()))
    print(f'#{test_case} {difference_max_min(N,list_condition)}')

# 15:07:10 실행이 완료되었습니다. 실행 시간 : 0.05580s
# 15:07:10 #1 630739
# #2 740510
# #3 838110
# 15:07:10 실행을 시작합니다.
# 15:07:10 성공적으로 컴파일 되었습니다.

# input
# 3
# 5
# 477162 658880 751280 927930 297191
# 5
# 565469 851600 460874 148692 111090
# 10
# 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

# output
# #1 630739
# #2 740510
# #3 838110