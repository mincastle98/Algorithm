# 영어 끝말잇기

def solution(n, words):
    answer = [0, 0]
    used = []
    expected = words[0][0]
    for idx, word in enumerate(words):
        if word in used or word[0] != expected:
            who = (idx + 1) % n
            when = (idx + 1) // n
            if who != 0: when += 1
            if who == 0: who = n
            return [who, when]
        else:
            used.append(word)
            expected = word[-1]

    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
