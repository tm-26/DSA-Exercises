from Input import checkifint


def fib(n):
    i = 1
    ans = 0
    while i <= n:
        ans = ans + fib2(i)
        i = i + 1
    return ans


def fib2(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fib2(i - 1) + fib2(i - 2)


if __name__ == '__main__':
    print("How many numbers of the fibonacci sequence would you like to add")
    n = checkifint()  # Validation
    ans = fib(n)

    print(f"Summation of = {ans}")
