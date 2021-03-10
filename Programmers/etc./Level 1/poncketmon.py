def solution(nums):
    nums_ = list(set(nums))
    if len(nums_) > len(nums) // 2:
        return len(nums) // 2
    else:
        return len(nums_)


print(solution([3, 1, 2, 3]))
