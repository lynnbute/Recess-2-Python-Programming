# A simple calculator
import module
import math as mt
from math import sqrt, factorial


def add(s, w):
    return (s+w)


def product(s, w):
    return (s*w)


print(module.product(8, 4))

print(sqrt(16))
print(factorial(6))

# Using alias
# mt is an alias for the library called "math"
print(mt.sqrt(25))

