#! /usr/bin/env python

def gcd(a, b):
    while b != 0:
        mod_value = a % b
        a = b
        b = mod_value
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def calculate_smallest_multiple(limit):
    result = 1
    for i in range(2, limit + 1):
        result = lcm(result, i)
    return result

print(calculate_smallest_multiple(20))