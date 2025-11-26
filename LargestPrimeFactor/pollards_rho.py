#! /usr/bin/env python

import random
import math

# Miller-Rabin --- 疑似素数判定（Pollard's rho に必須）
def is_prime(n):
    if n < 2:
        return False
    # 小さい素数で割り切れるかチェック
    for p in [2,3,5,7,11,13,17,19,23]:
        if n == p:
            return True
        if n % p == 0:
            return False

    # Miller-Rabin
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(5):  # 精度
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# Pollard's Rho
def pollards_rho(n):
    if n % 2 == 0:
        return 2
    if is_prime(n):
        return n  # その時点で素数

    # ランダムなスタート地点と定数
    x = random.randrange(2, n)
    y = x
    c = random.randrange(1, n)
    
    while True:
        # ウサギとカメの移動
        x = (pow(x, 2, n) + c) % n
        y = (pow(y, 2, n) + c) % n
        y = (pow(y, 2, n) + c) % n  # 2倍進む

        d = math.gcd(abs(x-y), n)
        if d == 1:
            continue
        if d == n:
            return pollards_rho(n)  # やり直し
        return d  # 素因数を発見


def factor(n):
    if n == 1:
        return []
    if is_prime(n):
        return [n]

    d = pollards_rho(n)
    return factor(d) + factor(n // d)


print(max(factor(600851475143)))
