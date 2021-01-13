//2020.06.07 (수정)
//프로그래머스 다리를 지나는 트럭 (큐)
//By Mincastle

#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Truck {
public:
    int outTime;
    int weight;

    Truck(int outTime, int weight) {
        this->outTime = outTime;
        this->weight = weight;
    }
};

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer;
    int time = 0;
    queue<Truck> onBridge;
    int now_weight = 0;
    reverse(truck_weights.begin(), truck_weights.end());

    while (!truck_weights.empty() || !onBridge.empty()) {
        time++;
        if (!onBridge.empty() && onBridge.front().outTime == time) {
            now_weight -= onBridge.front().weight;
            onBridge.pop();
        }

        if (!truck_weights.empty()) {
            if (now_weight + truck_weights.back() <= weight) {
                onBridge.push(Truck(time + bridge_length, truck_weights.back()));
                now_weight += truck_weights.back();
                truck_weights.pop_back();
            }
        }
    }

    answer = time;
    return answer;
}

int main(void) {
    vector<int> truck_weight = {7, 4, 5, 6};

    solution(2, 10, truck_weight);

    return 0;
}
