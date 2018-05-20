# Uses python3
import sys


def get_change(m, coins=(1, 3, 4)):
    #write your code here
    min_numb_coins = [0] * (m + 1)

    for i in range(1, m + 1):
        min_numb_coins[i] = 100000000
        for coin in coins:
            if i >= coin:
                num = min_numb_coins[i - coin] + 1
                if num < min_numb_coins[i]:
                    min_numb_coins[i] = num
    return min_numb_coins[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
