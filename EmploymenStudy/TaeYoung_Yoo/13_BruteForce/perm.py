# for문만으로 permutation구현한다.
# {1,2,3}에서 순열 경우의 수 나열하기

# 방법 1) 노가다
# for i in range(1,4):
#     for j in range(1,4):
#         if j != i:
#             for k in range(1,4):
#                 if k != i and k != j:
#                     print(i, j, k)


# 강점: 편하다
# 단점 만약 집합 내 원소의 수가 커진다면? 이거 다 구현하는거 불가능함

# 방법 2) 재귀
def perm(selected, remain):
    if not remain:
        print(selected)
    else:
        for i in range(len(remain)):
            select_i = remain[i]
            remain_list = remain[:i] + remain[i+1:]
            perm(selected+ [select_i], remain_list)

perm([], [1,2,3])