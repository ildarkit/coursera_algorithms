# Uses python3


def fib_iter(n):
    f = list()
    f.append(0)
    if n >= 1:
        f.append(1)
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f


if __name__ == '__main__':
    n = int(input())
    print(fib_iter(n))
