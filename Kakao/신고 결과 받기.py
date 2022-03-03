# 신고 결과 받기
def solution(id_list, report, k):
    answer = []
    report_log = dict()
    report_count = dict()
    for r in report:
        user, reported_user = r.split()
        if reported_user not in report_log.get(user, []):
            report_log[user] = report_log.get(user, []) + [reported_user]
            report_count[reported_user] = report_count.get(
                reported_user, 0) + 1

    for user in id_list:
        cnt = 0
        if user in report_log.keys():
            for reported in report_log[user]:
                if report_count[reported] >= k:
                    cnt += 1
        answer.append(cnt)

    return answer
