#! /usr/bin/env python

def generate_palindromes():
    for a in range(9, 0, -1):
        for b in range(9, -1, -1):
            for c in range(9, -1, -1):
                yield 100001*a + 10010*b + 1100*c  # 6桁回文

def find_largest_palindrome(min_factor, max_factor):
    for p in generate_palindromes():  # 大きい順
        for d in range(max_factor, min_factor - 1, -1):
            if p % d == 0:
                q = p // d
                if min_factor <= q <= max_factor:
                    return p

print(find_largest_palindrome(100, 999))
