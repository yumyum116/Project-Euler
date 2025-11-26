#! /usr/bin/env python

def calculate_factor(n):
    prime_array = []

    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            prime_array.append(i)
            n /= i
    
    return prime_array

print(calculate_factor(600851475143))