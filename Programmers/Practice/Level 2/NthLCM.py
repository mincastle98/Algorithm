# N개의 최소공배수
def solution(arr):
    answer = 1

    while arr:
        for i in range(2, arr[0] + 1):
            if arr[0] % i == 0:
                answer *= i
                for j in range(len(arr)):
                    if arr[j] % i == 0:
                        arr[j] //= i
                break
        if arr[0] == 1:
            arr = arr[1:]

    return answer


print(solution([2, 6, 8, 14]))
