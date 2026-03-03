def SectionSum(arr, N, M):
    '''
    :param arr: 구하고자하는 숫자가 들어있는 리스트
    :param N: 리스트의 길이
    :param M: 이웃하는 몇개를 합쳐서 값을 저장해야하는가
    :return: 이웃하는 값들의 합중 가장 큰값 리턴
    '''
    section_sum_list =[]
    for i in range(len(arr)-M+1):
        num = 0
        for j in range(M):
            num += arr[i+j]

        section_sum_list.append(num)

    return max(section_sum_list)- min(section_sum_list)


T = int(input())
for test_case in range(T):
    N, M = list(map(int, input().split()))
    arr =  list(map(int, input().split()))

    print(SectionSum(arr, N, M))





# input
# 3
# 10 3
# 1 2 3 4 5 6 7 8 9 10
# 10 5
# 6262 6004 1801 7660 7919 1280 525 9798 5134 1821
# 20 19
# 3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176