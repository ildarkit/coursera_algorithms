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


def merge(b, c, inv):
    d = []
    i = j = 0
    len_b = len(b)
    len_c = len(c)
    while i < len_b and j < len_c:
        if b[i] <= c[j]:
            d.append(b[i])
            i += 1
        else:
            inv += len(b[i:])
            d.append(c[j])
            j += 1
    while i < len_b:
        d.append(b[i])
        i += 1
    while j < len_c:
        d.append(c[j])
        j += 1
    return d, inv


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a)[1])