# 2022 KAKAO BLIND RECRUITMENT - 주차 요금 계산(Level 2)
import math
from collections import defaultdict


def convert_to_minutes(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute


def solution(fees, records):
    answer = []

    time_by_car = defaultdict(int)
    parkinglot = dict()

    for record in records:
        record = list(record.split())
        if record[2] == "IN":
            parkinglot[record[1]] = record[0]
        elif record[2] == "OUT":
            time_by_car[record[1]] += convert_to_minutes(record[0]) - convert_to_minutes(parkinglot[record[1]])
            parkinglot.pop(record[1])

    for car, time in parkinglot.items():
        time_by_car[car] += convert_to_minutes("23:59") - convert_to_minutes(time)

    for car in sorted(time_by_car):
        cost = fees[1]
        if time_by_car[car] - fees[0] > 0:
            cost += math.ceil((time_by_car[car] - fees[0]) / fees[2]) * fees[3]
        answer.append(cost)

    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

print(solution([120, 0, 60, 591],
               ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))

print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
