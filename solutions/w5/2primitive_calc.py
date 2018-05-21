# Uses python3
import sys


def optimal_sequence_origin(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def optimal_sequence(n):
    min_steps = [1]
    inxs = []
    k = len(min_steps)
    for i in range(k, n + 1):
        pairs = []
        inx = i - 1
        pairs.append((inx, min_steps[inx] + 1))
        if i % 3 == 0:
            inx = i // 3
            pairs.append((inx, min_steps[inx] + 1))
        if i % 2 == 0:
            inx = i // 2
            pairs.append((inx, min_steps[inx] + 1))
        min_ = min(pairs, key=lambda x: x[1])

        min_steps.append(min_[1])
        inxs.append(min_[0])

    numbers = []
    k = n
    while k > 0:
        numbers.append(k)
        k = inxs[k - 1]
    numbers.reverse()

    return numbers


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
         print(x, end=' ')
