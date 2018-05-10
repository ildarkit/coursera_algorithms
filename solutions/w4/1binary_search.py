# Uses python3
import sys


def binary_search_wrapper(a, x):
    left, right = 0, len(a)
    # write your code here
    return binary_search(a, left, right, x)


def binary_search(a, left, right, key):
    if right < left:
        return - 1
    mid = left + (right - left) // 2
    if mid > len(a) - 1:
        return -1
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary_search(a, left, mid - 1, key)
    else:
        return binary_search(a, mid + 1, right, key)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search_wrapper(a, x), end=' ')
