# Uses python3
import sys


def get_number_of_inversions(a, inv=0):
    inversions = inv
    n = len(a)
    if n == 1:
        return a, inversions
    med = n // 2
    b, inversions = get_number_of_inversions(a[:med], inversions)
    c, inversions = get_number_of_inversions(a[med:], inversions)
    aa, inversions = merge(b, c, inversions)
    return aa, inversions


def merge(x, y, inv):
    b = []
    len_y = len(y)
    while x and y:
        if x[0] <= y[0]:
            b.append(x.pop(0))
        else:
            inv += 1
            b.append(y.pop(0))
    if len(x):
        inv += len(x) * len_y  # ???
    if x:
        b.extend(x)
    elif y:
        b.extend(y)
    return b, inv


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a)[1])

