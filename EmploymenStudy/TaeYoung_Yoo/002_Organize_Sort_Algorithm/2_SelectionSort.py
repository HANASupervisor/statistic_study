# 선택 정렬
# 탐색돌리면서 가장 작은 최소값 찾고 그걸 앞에 넣고 다시 찾아서 앞에넣고 이런식으로 탐색
def SelectionSort(arr):
    for idx in range(len(arr)):
        minidx = idx
        for jdx in range(idx+1, len(arr)):
            if arr[minidx] > arr[jdx]:
                minidx = jdx

        arr[idx], arr[minidx] = arr[minidx], arr[idx]

    return arr

arr = [3,5,2,1]
print(SelectionSort(arr))

# [1, 3, 2, 5]