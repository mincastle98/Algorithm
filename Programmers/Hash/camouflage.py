# 위장
def solution(clothes):
    answer = 1
    clothesType = {}
    print(clothes)

    for n, t in clothes:
        if t not in clothesType:
            clothesType[t] = 1
        else:
            clothesType[t] += 1
    print(clothesType)

    for t in clothesType.values():
        answer *= t + 1
    answer -= 1

    print(answer)
    return answer


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
