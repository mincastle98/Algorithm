# 2018 KAKAO BLIND RECRUITMENT - 캐시(Level 2)
def solution(cacheSize, cities):
    cities = list(map(lambda x: x.upper(), cities))

    cache_cnt = dict()
    cache = set()

    exec_time = 0
    if cacheSize == 0:
        return len(cities) * 5

    for i, city in enumerate(cities):
        if city in cache:  # hit
            cache_cnt[city] = i + 1
            exec_time += 1
        else:  # miss
            if len(cache) >= cacheSize:
                lru_cnt = min([cache_cnt[c] for c in cache])
                lru = list(cache_cnt.keys())[list(cache_cnt.values()).index(lru_cnt)]
                cache.remove(lru)

            cache.add(city)
            cache_cnt[city] = i + 1
            exec_time += 5

    return exec_time


ex1 = [3, 3, 2, 5, 2, 0]
ex2 = [["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],
       ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"],
       ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
        "Rome"],
       ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
        "Rome"],
       ["Jeju", "Pangyo", "NewYork", "newyork"],
       ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]]

for e1, e2 in zip(ex1, ex2):
    print(solution(e1, e2))
