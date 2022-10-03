from collections import defaultdict


def solution(genres, plays):
    answer = []

    genres_songs = defaultdict(list)
    genres_hits = defaultdict(int)
    for i, v in enumerate(zip(genres, plays)):
        genres_songs[v[0]] += [(i, v[1])]
        genres_hits[v[0]] += v[1]

    candidates_songs = []
    for genre, songs in genres_songs.items():
        songs.sort(key=lambda x: x[0])
        songs.sort(key=lambda x: x[1], reverse=True)
        candidates_songs.append((genres_hits[genre], songs[:2]))

    candidates_songs.sort(key=lambda x: x[0], reverse=True)
    for songs in candidates_songs:
        answer += list(map(lambda x: x[0], songs[1]))

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
