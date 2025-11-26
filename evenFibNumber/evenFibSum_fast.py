"""
 
 # Approach
   Using the relation among even Fibonacci numbers:
        fib(n) = 4 * fib(n - 1) + fib(n - 2),
   we only compute even Fibonacci numbers and sum them.

"""

#! /usr/bin/env python

def evenFibSum_fast(limit):
    even_fib1 = 2
    even_fib2 = 8
    sum = even_fib1
    
    while even_fib2 < limit:
        sum += even_fib2
        next_even_value = 4 * even_fib2 + even_fib1
        even_fib1 = even_fib2
        even_fib2 = next_even_value
    
    return sum

print(evenFibSum_fast(4 * 12e6))