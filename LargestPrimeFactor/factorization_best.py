#! /usr/bin/env python

def largest_prime_factor(n):
    # まず 2 で割り切れるだけ割る
    while n % 2 == 0:
        max_prime = 2
        n //= 2

    # 3から奇数だけ √n まで試す
    i = 3
    while i * i <= n:
        while n % i == 0:
            max_prime = i
            n //= i
        i += 2  # 偶数は試さない

    # 最後に n が 1 以上ならそれ自体が素数
    if n > 1:
        max_prime = n

    return max_prime


print(largest_prime_factor(600851475143))
