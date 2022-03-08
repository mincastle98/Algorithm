# 13305 - 주유소(S4)
import sys

N = int(sys.stdin.readline())
dists = list(map(int, sys.stdin.readline().split()))
stations = list(map(int, sys.stdin.readline().split()))

i = 0
price = 0
while i < len(stations)-1:
    j = 1
    while i+j < len(stations) and stations[i] < stations[i+j]:
        j += 1
    price += stations[i] * sum(dists[i:i+j])
    i = i+j

print(price)
