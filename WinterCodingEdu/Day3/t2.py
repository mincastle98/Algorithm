N, x = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 2, 0   # 탐색 실패 결과 설정

# 시작지점 탐색
low, high = 0, N-1
while low <= high:
    mid = (low + high) // 2

    if arr[mid] == x:
        if mid == 0 or arr[mid-1] != arr[mid]:
            start = mid
            break

    if x > arr[mid]:
        low = mid + 1
    else:
        high = mid - 1

# 종료지점 탐색
low, high = 0, N-1
while low <= high:
    mid = (low + high) // 2

    if arr[mid] == x:
        if mid == N-1 or arr[mid+1] != arr[mid]:
            end = mid
            break

    if x >= arr[mid]:
        low = mid + 1
    else:
        high = mid - 1

print(end-start+1)
