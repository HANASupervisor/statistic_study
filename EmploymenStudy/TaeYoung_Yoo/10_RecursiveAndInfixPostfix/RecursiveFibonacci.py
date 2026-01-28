def RecursiveFibonacci(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return RecursiveFibonacci(num-1) + RecursiveFibonacci(num-2)


print(RecursiveFibonacci(5))


