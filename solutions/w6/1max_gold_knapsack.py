# Uses python3
import sys


def optimal_weight_origin(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


def optimal_weight(W, w):
    len_w = len(w)
    value = [[0] for _ in range(W + 1)]
    value[0] = [0 for _ in range(len_w + 1)]
    for i in range(1, len_w + 1):
        for j in range(1, W + 1):
            value[j].append(value[j][i - 1])
            if w[i - 1] <= j:
                val = value[j - w[i - 1]][i - 1] + w[i - 1]
                if value[j][i] < val:
                    value[j][i] = val
    return value

# @TODO implement search for items
# def find_items(value, w, k , s, items=None):
#     if value[k][s] == 0:
#         return items
#     if value[k - 1][s] == value[k][s]:
#         items = find_items(value, w, k - 1, s, items)
#     else:
#         items = find_items(value, w, k - 1, s - w[k], items)
#         if items is None:
#             items = []
#         items.append(k)
#     return items
#
#
# def find_optimal_weight_items(W, w):
#     items = []
#     value = optimal_weight(W, w)
#     find_items(value, w, W, len(w), items)
#     return value[-1][-1], items


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w)[-1][-1])
