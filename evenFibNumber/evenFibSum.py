#! /usr/bin/env python

def evenFibSum(limit):
    a = 1
    b = 2
    sum = 0

    while a < limit:
        if a % 2 == 0:
            sum += a
        next_value = a + b
        a = b
        b = next_value
    
    return sum

print(evenFibSum(4 * 12e6))
