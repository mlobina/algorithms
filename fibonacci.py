
def Fibonacci_num():
    n = int(input('Введите номер искомого элемента: '))
    if n < 2:
        print(f'Искомый элемент равен {n}')
    else:
        i = 2
        fibo = [0, 1, 1]
        while i <= n:
            fibo[2] = fibo[0] + fibo[1]
            fibo[0] = fibo[1]
            fibo[1] = fibo[2]
            i += 1
        print(f'Искомый элемент равен {fibo[1]}')


def Fibonacci_num_other():
    left = 0
    right = 1
    n = int(input('Введите номер искомого элемента: '))
    if n < 2:
        print(f'Искомый элемент равен {n}')
    else:
       for i in range(n):
           cur = left + right
           left = right
           right = cur
       print(f'Искомый элемент равен {left}')


def Fibonacci_num_third():
    n = int(input('Введите номер искомого элемента: '))

    fib = [0, 1] + [0]*(n - 1)

    for i in range(2, n + 1):
        fib[i] = fib[i -1] + fib[i - 2]
        print(fib[i], end=' ')

    print(f'Искомый элемент {fib[n]}')







