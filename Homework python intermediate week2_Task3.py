def fib_generator(num: int):
    fib1, fib2 = 0, 1
    print(fib1, fib2, end=' ')
    for i in range(2, num):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')
    print()


def fib_list(num: int):
    list = []
    fib1, fib2 = 0, 1
    list.append(fib1)
    list.append(fib2)
    for i in range(2, num):
        fib1, fib2 = fib2, fib1 + fib2
        list.append(fib2)
    print(list)


fib_generator(10)
fib_list(10)
