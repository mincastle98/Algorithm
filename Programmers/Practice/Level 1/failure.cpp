//2020.06.06
//프로그래머스 실패율 (2019 KAKAO BLIND RECRUITMENT)
//By Mincastle

#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<double> failure;

    sort(stages.begin(), stages.end(), greater<int>());

    for (int i = 0; i <= N; i++) {
        int cnt = 0;
        double total = stages.size();

        if (stages.empty()) {
            failure.push_back(0);
            continue;
        }

        while (stages.back() == i + 1) {
            stages.pop_back();
            cnt++;
        }
        failure.push_back((total - stages.size()) / total);
    }

    for (int i = 0; i < failure.size(); i++) {
        int idx = max_element(failure.begin(), failure.end()) - failure.begin() + 1;

        if (idx <= N) answer.push_back(idx);
        failure[idx - 1] = -1;
    }

    return answer;
}

int main(void) {
    vector<int> stages = {2,1,2,6,2,4,3,3};

    solution(5, stages);

    return 0;
}