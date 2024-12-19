from functools import lru_cache
from math import gcd, inf
import numpy as np


def is_possible(a, b, c):
    return (c[0] % gcd(a[0], b[0]) == 0) and (c[1] % gcd(a[1], b[1]) == 0)


# Cramers rule, instant for both parts
def get_cost_2(a, b, c):
    if not is_possible(a, b, c):
        return 0
    an = (c[0]*b[1] - c[1]*b[0]) // (a[0]*b[1] - a[1]*b[0])
    bn = (a[0]*c[1] - a[1]*c[0]) // (a[0]*b[1] - a[1]*b[0])
    if an * a[0] + bn * b[0] == c[0] and an * a[1] + bn * b[1] == c[1]:
        return an*3 + bn
    return 0

# Recursion, not feasible for P2


def get_cost(a, b, c, max_i):
    if not is_possible(a, b, c):
        return 0

    min_cost = inf

    @lru_cache(maxsize=None)
    def traverse(pos, cost, i_a, i_b):
        nonlocal min_cost
        if pos[0] > c[0] or pos[1] > c[1]:
            return
        if i_a > max_i or i_b > max_i:
            return
        if pos[0] == c[0] and pos[1] == c[1]:
            if cost < min_cost:
                min_cost = cost
            return

        traverse((pos[0] + a[0], pos[1] + a[1]), cost + 3, i_a+1, i_b)
        traverse((pos[0] + b[0], pos[1] + b[1]), cost + 1, i_a, i_b+1)

    traverse((0, 0), 0, 0, 0)
    if min_cost == inf:
        return 0
    return min_cost


input = open("input").read().strip()
lines = [line for line in input.split("\n")]

sum1 = 0
sum2 = 0
for i in range(len(lines)//3):
    a = [int(x) for x in lines[3*i+0].split(" ")]
    b = [int(x) for x in lines[3*i+1].split(" ")]
    c = [int(x) for x in lines[3*i+2].split(" ")]
    c2 = [int(x) + 10000000000000 for x in lines[3*i+2].split(" ")]
    sum1 += get_cost_2(a, b, c)
    sum2 += get_cost_2(a, b, c2)

print(sum1)
print(sum2)
