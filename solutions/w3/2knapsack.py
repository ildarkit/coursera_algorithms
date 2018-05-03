# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    items = sorted(zip(values, weights), key=lambda item: item[0] / item[1], reverse=True)
    for item in items:
        if capacity == 0:
            break
        a = item[1] if item[1] < capacity else capacity
        value += a * (item[0] / item[1])
        capacity -= a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
