import functools

def compare(a, b):
    if a+b > b+a: return -1
    else: return 1

def solution(numbers):
    answer = ''
    tmp = []

    for i in numbers:
        tmp.append(str(i))
    tmp = sorted(tmp, key=functools.cmp_to_key(compare))

    if tmp[0] == '0': return '0'
    for i in tmp:
        answer += i

    return answer