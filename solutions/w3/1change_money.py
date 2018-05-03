# Uses python3
import sys

COINS = (10, 5, 1)


def get_change(m):
    #write your code here
    i = 0
    coin = COINS[i]
    count = 0
    while m > 0:
        while m >= coin:
            m -= coin
            count += 1
        if i < len(COINS) - 1:
            i += 1
            coin = COINS[i]
    return count


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
