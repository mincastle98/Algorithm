# 신규 아이디 추천
def solution(new_id):
    answer = ''

    new_id = new_id.lower()  # 1

    removed = 0
    for idx in range(len(new_id)):
        idx -= removed
        if idx >= len(new_id): break
        if new_id[idx] != "." and new_id[idx] != "-" and new_id[idx] != "_":
            if 48 <= ord(new_id[idx]) <= 57 or 97 <= ord(new_id[idx]) <= 122:
                continue
            else:
                new_id = new_id[:idx] + new_id[idx + 1:]
                removed += 1
        else:
            continue  # 2

    while True:
        old_id = new_id
        new_id = new_id.replace("..", ".")
        if old_id == new_id:
            break   # 3

    if new_id and new_id[0] == ".":
        new_id = new_id[1:]
    if new_id and new_id[-1] == ".":
        new_id = new_id[:-1]  # 4

    if not new_id:
        new_id = "a"  # 5

    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id and new_id[-1] == ".":
        new_id = new_id[:-1]  # 6

    while len(new_id) < 3:
        new_id += new_id[-1]  # 7

    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
