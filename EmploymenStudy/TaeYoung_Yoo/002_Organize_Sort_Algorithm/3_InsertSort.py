# insert sort
# 왼쪽과 오른쪽으로 리스트를 분해해서 왼쪽은 정렬 오른쪽은 정렬이 안되었다고 판단하고
# 하나씩 정렬시키며 맞춰가는 방법
def InsertSort(arr):
    # 정렬된 리스트 하나씩 키우기
    for idx in range(1, len(arr)):
        # 실제 값들 비교해서 움직이기
        for jdx in range(idx-1, -1, -1):
            # 만약 오른쪽에 있는 값이 왼쪽값보다 클경우 위치 바꾸기
            if arr[jdx+1] < arr[jdx]:
                arr[jdx+1], arr[jdx] = arr[jdx], arr[jdx+1]


    return arr


arr = [3,5,2,1]
print(InsertSort(arr))