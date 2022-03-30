# 14889 - 스타트와 링크(S1)
from itertools import combinations
import math

N = int(input())
synergy = [list(map(int, input().split())) for _ in range(N)]

comb = list(combinations(range(N), N//2))
comb_team = list(map(lambda i: (comb[i], comb[-(i+1)]), range(len(comb)//2)))

min_gap = math.inf
for t in comb_team:
    ability_a, ability_b = 0, 0

    comb_mem = list(combinations(t[0], 2))
    for m in comb_mem:
        ability_a += synergy[m[0]][m[1]]
        ability_a += synergy[m[1]][m[0]]

    comb_mem = list(combinations(t[1], 2))
    for m in comb_mem:
        ability_b += synergy[m[0]][m[1]]
        ability_b += synergy[m[1]][m[0]]

    min_gap = min(min_gap, abs(ability_a-ability_b))

print(min_gap)
