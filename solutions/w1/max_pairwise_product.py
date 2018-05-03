# Uses python3


def max_product(n, a):
    inx = 0
    for i in range(1, n):
        if a[i] > a[inx]:
            inx = i

    a[inx], a[n - 1] = a[n - 1], a[inx]
    inx = 0
    for i in range(1, n - 1):
        if a[i] > a[inx]:
            inx = i
    a[inx], a[n - 2] = a[n - 2], a[inx]
    return a[n - 2] * a[n - 1]


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert (len(a) == n)
    print(max_product(n, a))

