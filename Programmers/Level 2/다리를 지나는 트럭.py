# 다리를 지나는 트럭(Level 2)
def solution(bridge_length, weight, truck_weights):
    bridge_idx = 0  # 다리 위 선두 트럭 index
    truck_idx = 1  # 지나가야 할 트럭 index
    passed_truck_idx = 0  # 지나간 트럭 수

    time = 1  # 현재 시각
    on_bridge_weight = truck_weights[0]  # 다리 위 무게 총합
    bridge = [time]  # 입장 시각
    while True:
        time += 1
        if bridge[bridge_idx] + bridge_length == time:
            on_bridge_weight -= truck_weights[passed_truck_idx]
            passed_truck_idx += 1
            bridge_idx += 1
        if truck_idx < len(truck_weights) and on_bridge_weight + truck_weights[truck_idx] <= weight:
            bridge.append(time)
            on_bridge_weight += truck_weights[truck_idx]
            truck_idx += 1

        if bridge_idx == len(truck_weights) and truck_idx == len(truck_weights):
            break

    return time


testcases = [(2, 10, [7, 4, 5, 6]),
             (100, 100, [10]),
             (100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])]
for tc in testcases:
    print(solution(tc[0], tc[1], tc[2]))
