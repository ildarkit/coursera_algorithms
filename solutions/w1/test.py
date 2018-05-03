import random

import max_pair_product_naive
import max_pairwise_product

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    while True:
        n = random.randint(2, a)
        m = []
        for _ in range(n):
            m.append(random.randint(0, b))
        print(m)
        res1 = max_pair_product_naive.max_naive(n, m)
        res2 = max_pairwise_product.max_product(n, m)
        if res1 == res2:
            print('OK')
        else:
            print('Wrong answer: ', res1, res2)
            break
