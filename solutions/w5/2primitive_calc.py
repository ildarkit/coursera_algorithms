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
    sequence = [1]
    i = 1
    while i < n:

        min_else = 100_000_000
        if i + 1 >= sequence[i - 1] - 1:
            min1 = sequence[i - 1] + 1
        else:
            min1 = min_else
        if i + 1 >= sequence[i - 1] * 2:
            min2 = sequence[i // 2] + 1
        else:
            min2 = min_else
        if i + 1 >= sequence[i - 1] * 3:
            min3 = sequence[i // 3] + 1
        else:
            min3 = min_else
        sequence.append(min(min1, min2, min3))
        i += 1
    return sequence


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
