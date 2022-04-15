# MaximumXORofTwoNumbersinanArray
from typing import List


def findMaximumXOR(nums):
    bits = dict()
    for num in nums:
        key = num

        idx = 0
        while num:
            print(bin(num >> idx & 1))
            bits[key] = bits.get(key, []) + ([idx] if (bin(num >> idx & 1)) == '0b1' else [])
            num >>= idx
            idx += 1


findMaximumXOR([3, 10, 5, 25, 2, 8])
# 1100
