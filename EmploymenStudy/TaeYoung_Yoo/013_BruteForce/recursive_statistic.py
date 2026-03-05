# 맨손 코딩

# 재귀로 순열 계산
def permutation(selected, remain):
    if not remain:
        print(selected)
    else:
        for i in range(len(remain)):
            select_i = remain[i]
            remain_list = remain[:i] + remain[i + 1:]
            permutation(selected + [select_i], remain_list)

permutation([], [1,2,3])

# 재귀로 조합 계산
def combination(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]
    else:
        for i in range(len(arr)):
            elem = arr[i]
            for rest in combination(arr[i+1:], n-1):
                result.append([elem] + rest)

    return result

print(combination([1,2,3],2))