# 2019 카카오 개발자 겨울 인턴십 - 튜플(Level 2)
def solution(s):
    answer = []
    set_list = s.split("},{")
    set_list[0] = set_list[0].lstrip("{")
    set_list[-1] = set_list[-1].rstrip("}")

    set_list = list(map(lambda x: x.split(","), set_list))
    set_list.sort(key=len)

    for s in set_list:
        answer.append((list(set(s) - set(answer))[0]))
    answer = list(map(int, answer))

    return answer


ex = ["{{2},{2,1},{2,1,3},{2,1,3,4}}",
      "{{1,2,3},{2,1},{1,2,4,3},{2}}",
      "{{20,111},{111}}", "{{123}}",
      "{{4,2,3},{3},{2,3,4,1},{2,3}}"]

for e in ex:
    print(solution(e))
