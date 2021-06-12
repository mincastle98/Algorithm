# 2606 - 바이러스

def solution(computer, pairs):
    network = []
    for p in pairs:
        flag = 1
        for n in network:
            if p[0] in n or p[1] in n:
                flag = 0
                n |= set(p)
        if flag:
            network.append({p[0], p[1]})

    while True:
        flag = 0
        for idx1, n1 in enumerate(network):
            for idx2, n2 in enumerate(network):
                if not n1 == n2 and n1 & n2:
                    flag = 1
                    network[idx1] |= n2
                    del (network[idx2])
                    break
            if flag: break
        if not flag: break

    # 2606 - 바이러스

    def solution(computer, pairs):
        network = []
        for p in pairs:
            flag = 1
            for n in network:
                if p[0] in n or p[1] in n:
                    flag = 0
                    n |= set(p)
            if flag:
                network.append({p[0], p[1]})

        while True:
            flag = 0
            for idx1, n1 in enumerate(network):
                for idx2, n2 in enumerate(network):
                    if not n1 == n2 and n1 & n2:
                        flag = 1
                        network[idx1] |= n2
                        del (network[idx2])
                        break
                if flag: break
            if not flag: break

        for c in range(1, computer + 1):
            flag = 1
            for n in network:
                if str(c) in n:
                    flag = 0
                else:
                    break
            if flag:
                network.append({str(c)})

        for n in network:
            if '1' in n:
                print(len(n) - 1)
                break

    a = int(input())
    b = int(input())
    c = []
    for _ in range(b):
        c.append(input().split())

    solution(a, c)

    for c in range(1, computer + 1):
        flag = 1
        for n in network:
            if str(c) in n:
                flag = 0
            else:
                break
        if flag:
            network.append({str(c)})

    for n in network:
        if '1' in n:
            print(len(n) - 1)
            break


a = int(input())
b = int(input())
c = []
for _ in range(b):
    c.append(input().split())

solution(a, c)
