# 카운팅 정렬
# 인덱스를 활용해서 인덱스 번호와 매칭해서 해당 숫자가 몇번 나왔는지를 정리하고
# 누적합을 통해 몇번까지 무슨숫자가 오게할지를 설정하고
# 누적합의 인덱스를 통해 해당숫자를 찾고 누적합 값을 통해 해당 인덱스가 결과리스트의 몇번째인덱스에
# 들어가야하는지 알수있으니 그걸로 결과리스트에 해당인덱스값을 채우고 누적합인덱스에서 -1을해준다.
def CountingSort(arr):
    counting_list = [0] * (max(arr)+1)
    result = [0] * len(arr)
    # arr을 순회하면서 인자에 값에 해당하는 counting_list의 인덱스에 해당하는값을 1씩 증가시킨다.
    for idx in range(len(arr)):
        counting_list[arr[idx]] += 1

    # 카운팅 리스트가 제대로 나왔으면 이제 누적합리스트를 만들어준다.
    for jdx in range(1, len(counting_list)):
        counting_list[jdx] = counting_list[jdx-1] + counting_list[jdx]

    # 누적합이 제대로 떴으니 이제 result리스트를 만들어보자
    for kdx in range(len(arr)-1, -1, -1):
        result[counting_list[arr[kdx]]-1] = arr[kdx] # 원본에 있는 값을 차례대로 넣어야한다.
        counting_list[arr[kdx]] -= 1


    return result


arr = [3,5,3,2,1]
print(CountingSort(arr))