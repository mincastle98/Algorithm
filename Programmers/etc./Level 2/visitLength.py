# 방문 길이
def solution(dirs):
    axis = [0, 0]
    visited = []
    for d in dirs:
        if d == "U":
            if axis[1] == 5: continue
            line = [axis[:], [axis[0], axis[1] + 1]]
            line.sort()
            if line not in visited:
                visited.append(line)
            axis[1] += 1
        elif d == "D":
            if axis[1] == -5: continue
            line = [axis[:], [axis[0], axis[1] - 1]]
            line.sort()
            if line not in visited:
                visited.append(line)
            axis[1] -= 1
        elif d == "R":
            if axis[0] == 5: continue
            line = [axis[:], [axis[0] + 1, axis[1]]]
            line.sort()
            if line not in visited:
                visited.append(line)
            axis[0] += 1
        elif d == "L":
            if axis[0] == -5: continue
            line = [axis[:], [axis[0] - 1, axis[1]]]
            line.sort()
            if line not in visited:
                visited.append(line)
            axis[0] -= 1

    return len(visited)


print(solution("ULURRDLLU"))
