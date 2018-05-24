# Uses python3
import sys
import itertools


def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            # sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)
            sums_ = 0
            for k in range(len(A)):
                if c[k] == i:
                    sums_ += A[k]
            sums[i] = sums_
        if sums[0] == sums[1] == sums[2]:
            return 1

    return 0


# @TODO implement with dynamic programming approach
def partition3_dp(souvenirs):
    pass


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

