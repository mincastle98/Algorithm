# 캐시
def solution(cacheSize, cities):
    answer = 0
    cache = []

    if cacheSize == 0:
        return len(cities) * 5

    for c in cities:
        c = c.lower()
        if c in cache:
            idx = cache.index(c)
            cache = cache[0:idx] + cache[idx + 1:] + [c]
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache = cache[1:] + [c]
            else:
                cache.append(c)
            answer += 5

    return answer


print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
