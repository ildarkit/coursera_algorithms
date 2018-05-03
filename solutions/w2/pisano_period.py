# Uses python3


def pesano(n, m):
    f = list()
    f.append(0)
    if n >= 1:
        f.append(1)
    for i in range(2, n + 1):
        f.append((f[i - 1] + f[i - 2]) % m)
    return f


if __name__ == '__main__':
    p = map(int, input().split())
    print(pesano(*p))