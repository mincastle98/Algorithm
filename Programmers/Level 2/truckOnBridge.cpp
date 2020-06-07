//2020.06.07
//프로그래머스 다리를 지나는 트럭 (큐)
//By Mincastle

#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

queue<int> queuePlus1(queue<int> q) {
    queue<int> temp;
    int n = q.size();
    for (int i = 0; i < n; i++) {
        temp.push(q.front() + 1);
        q.pop();
    }
    return temp;
}

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 1;
    queue<int> onBridge;
    int now_weight = 0;
    int check;
    queue<int> sameCnt;
    reverse(truck_weights.begin(), truck_weights.end());

    while (!truck_weights.empty() || !onBridge.empty()) {
        if (!truck_weights.empty()) {
            int wait_truck = truck_weights.back();
            if (now_weight + wait_truck <= weight) {
                now_weight += wait_truck;
                truck_weights.pop_back();
                if (wait_truck == truck_weights.back())
                    sameCnt.push(1);
                for (int i = 0; i < bridge_length - onBridge.size();) {
                    onBridge.push(wait_truck);
                }
            }
        }

        check = onBridge.front();
        onBridge.pop();

        if (onBridge.front() != check) {
            now_weight -= check;
        }
        if (!sameCnt.empty() && sameCnt.front() == bridge_length) {
            now_weight -= check;
            sameCnt.pop();
        }

        sameCnt = queuePlus1(sameCnt);
        answer++;
    }

    return answer;
}

int main(void) {
    vector<int> truck_weight = {1, 2, 3, 4, 4, 3, 1};

    solution(8, 18, truck_weight);

    return 0;
}
