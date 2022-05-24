def fib_generator(n: int):
    count = 0
    fib1, fib2 = 0, 1
    while count < n:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2
        count += 1


def fib_list(n: int):
    list_fib = [0]
    count = 0
    fib1, fib2 = 0, 1
    while count < n:
        yield list_fib
        fib1, fib2 = fib2, fib1 + fib2
        count += 1
        list_fib.append(fib1)


for result1 in fib_generator(3):
    print(result1)
print('-' * 25)
for result2 in fib_list(3):
    print(result2)
