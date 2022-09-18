## Add code below with answer clearly stated


def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(int(n / 10))


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(sum_of_digits(factorial(100)))
