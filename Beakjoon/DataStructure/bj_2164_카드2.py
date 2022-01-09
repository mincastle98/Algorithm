# 2164 - 카드2
from collections import deque

N = int(input())
cards = deque([i+1 for i in range(N)])

while len(cards) != 1:
    cards.popleft()
    card = cards.popleft()
    cards.append(card)

print(cards[0])
