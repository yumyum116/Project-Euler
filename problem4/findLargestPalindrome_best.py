#! /usr/bin/env python

def find_largest_palindrome():
    for a in range(9, 0, -1):
        for b in range(9, -1, -1):
            for c in range(9, -1, -1):
                p = 100001*a + 10010*b + 1100*c  # 6桁回文（大きい順）
                r = int(p**0.5)
                for d in range(r, 100, -1):
                    if p % d == 0:
                        e = p // d
                        if 100 <= e <= 999:
                            return p

print(find_largest_palindrome())
