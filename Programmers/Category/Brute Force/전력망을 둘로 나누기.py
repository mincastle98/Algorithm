import math
from collections import defaultdict
from copy import deepcopy


def solution(n, wires):
    answer = math.inf
    nodes = defaultdict(list)
    for wire in wires:
        nodes[wire[0]] += [wire[1]]
        nodes[wire[1]] += [wire[0]]

    for i in range(len(wires)):
        tmp_nodes = deepcopy(nodes)
        disconnected = wires[i]
        tmp_nodes[disconnected[0]].pop(tmp_nodes[disconnected[0]].index(disconnected[1]))
        tmp_nodes[disconnected[1]].pop(tmp_nodes[disconnected[1]].index(disconnected[0]))

        visited = [False] * n
        cnts = []
        for i in range(2):
            stack = [visited.index(False) + 1]
            visited[stack[0] - 1] = True
            cnt = 1
            while stack:
                now = stack.pop()
                for node in tmp_nodes[now]:
                    if not visited[node - 1]:
                        stack.append(node)
                        visited[node - 1] = True
                        cnt += 1

            cnts.append(cnt)
        answer = min(abs(cnts[0] - cnts[1]), answer)

    return answer


testcases = [[9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]],
             [4, [[1, 2], [2, 3], [3, 4]]],
             [7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]]]

for testcase in testcases:
    print(solution(testcase[0], testcase[1]))
