x = int(input())
table = [0, 0]  # 해당 인덱스에 해당하는 값을 만드는데 소요되는 최소 비용

for i in range(2, x+1):
    # d 연산
    table.append(table[i-1]+1)
    # a 연산
    if i % 5 == 0:
        table[i] = min(table[i], table[i//5]+1)
    # b 연산
    if i % 3 == 0:
        table[i] = min(table[i], table[i//3]+1)
    # c 연산
    if i % 2 == 0:
        table[i] = min(table[i], table[i//2]+1)

print(table[x])
