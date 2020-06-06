//2020.06.05
//프로그래머스 예산 (Summer/Winter Coding(~2018))

#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;

    sort(d.begin(), d.end(), greater<int>());

    while (budget >= d.back() && budget != 0&&!d.empty()) {
        budget -= d.back();
        d.pop_back();
        answer++;
    }

    return answer;
}

int main(void) {
    vector<int> d = {2, 2, 3, 3};

    solution(d, 10);

    return 0;
}