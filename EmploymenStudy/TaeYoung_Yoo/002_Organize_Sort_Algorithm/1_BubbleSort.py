# 버블 정렬
# 인접한 수를 확인하면서 가장 큰값 먼저 정렬하는 방법
def BubbleSort(arr):
    for idx in range(len(arr)):
        for jdx in range(len(arr)-1-idx):
            if arr[jdx] > arr[jdx+1]:
                arr[jdx], arr[jdx+1] = arr[jdx+1], arr[jdx]

    return arr


arr =[3,5,2,1]
print(BubbleSort(arr))