#! /usr/bin/env python

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def find_largest_palindrome(min_factor, max_factor):
    best = 0
    for a in range(max_factor, min_factor - 1, -1):
        for b in range(a, min_factor - 1, -1):
            prod = a * b
            if prod <= best:
                break
            if is_palindrome(prod):
                best = prod
                break
    return best

print(find_largest_palindrome(100, 999))

