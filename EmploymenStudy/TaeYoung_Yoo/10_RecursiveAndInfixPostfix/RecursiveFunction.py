def practice_recursive2(x):
    x += 1
    print(f'in function2 {x}')


def practice_recursive1(x):
    x += 1
    print(f'in function1 {x}')
    practice_recursive2(x)
    print(f'out function1 {x}')

def practice_recursive():
    x = 3
    print(f'before {x}')
    practice_recursive1(x)
    print(f'after {x}')



practice_recursive()