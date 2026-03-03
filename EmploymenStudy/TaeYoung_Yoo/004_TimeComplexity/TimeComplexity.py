# 시간 복잡도 중요함? 그거 필요 없다고 생각하는데
# 코딩할때 얼마나 차이가 나는지 보여드림

import timeit
# 데이터 준비
N = 1000000
arr= list(range(1,N+1))

def Summation(arr):
    summation_number = 0
    for num in arr:
        summation_number += num

    return summation_number

def Gaussian_Sum(arr):
    N = len(arr)
    summation_number = N*(N+1)/2
    return summation_number

#
t1 = timeit.timeit(stmt='Summation(arr)',
                   globals=globals(),
                   number = 10
                   )
t2 = timeit.timeit(stmt='Gaussian_Sum(arr)',
                   globals=globals(),
                   number= 10
                   )

print(f'Summation: {t1}')
print(f'Gaussian_Sum: {t2}')
print(f'속도차이: {t1/t2}')

# summation: 0.34929150000000003
# gaussian: 3.7999999999982492e-06
# 속도차이: 91918.81578951604