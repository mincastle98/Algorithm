# N개의 최소공배수
def solution(arr):
    answer = 1

    arr.sort()
    for a in arr:
        answer *= a
        for j in range(len(arr)):
            if arr[j] % a == 0:
                arr[j] //= a

    return answer


print(solution([2, 6, 8, 14]))
