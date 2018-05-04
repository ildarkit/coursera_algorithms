# Uses python3

import sys


def greater_or_equal(a, b):
    result = False
    len_a = len(a)
    len_b = len(b)
    if len_a != len_b:
        l = len_a - len_b
        if l < 0:
            l = - l
        if int(b) // (10 ** l) <= int(a) and len_a < len_b:
            result = True
    elif int(a) >= int(b):
        result = True
    return result


def largest_number(a):
    # write your code here
    res = ""
    while a:
        _max = a[0]
        counter = 1
        n = len(a)
        for i in range(1, n):
            if greater_or_equal(a[i], _max):
                if _max == a[i]:
                    counter += 1
                else:
                    counter = 1
                _max = a[i]
        res += _max * counter
        b = []
        for x in a:
            if x != _max:
                b.append(x)
        a = b
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

