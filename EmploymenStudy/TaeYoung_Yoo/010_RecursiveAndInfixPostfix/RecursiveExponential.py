# 두개의 정수 a와 n이 주어질때 a**n을 재귀로 구해봐라
def power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(a, n/2) * power(a, n/2)
    elif n % 2 == 1:
        return a * power(a, n//2) * power(a, n//2)

print(power(3,4))

# power(3,4) = power(3,2) * power(3,2)
# power(3,2) = power(3,1) * power(3,1)
# power(3,1) = 3*power(3,0) * power(3,0)
# power(3,0) = 1
# power(3,1) = 3*1*power(3,0)
# power(3,0) = 1
# power(3,1) = 3
# power(3,2) = 3 * power(3,1)
# power(3,1) = 3*power(3,0)*power(3,0)
# power(3,0) = 1
# power(3,1) = 3*1*power(3,0)
# power(3,0) = 1
# power(3,1) = 3
# power(3,2) = 3*3
# power(3,4) = 9*power(3,2)
# power(3,2) = power(3,1) * power(3,1)
# power(3,1) = 3*power(3,0) * power(3,0)
# power(3,0) = 1
# power(3,1) = 3*1*power(3,0)
# power(3,0) = 1
# power(3,1) = 3
# power(3,2) = 3 * power(3,1)
# power(3,1) = 3*power(3,0)*power(3,0)
# power(3,0) = 1
# power(3,1) = 3*1*power(3,0)
# power(3,0) = 1
# power(3,1) = 3
# power(3,2) = 3*3
# power(3,4) = 9*9 = 81


