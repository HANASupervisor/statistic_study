# {1,2,3}중에 2개를 순서 고려안하고 뽑는 경우를 생각해보자
def Combination(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in Combination(arr[i+1:], n-1):
            result.append([elem]+rest)

    return result

print(Combination([1,2,3,4], 3))