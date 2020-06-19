//2020.06.18
//프로그래머스 탑 (스택)
//By Mincastle

#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> heights) {
    vector<int> answer(heights.size());
    stack<int> signal;

    for (int i = heights.size() - 1; i >= 0; i--) {
        if (signal.empty()) signal.push(heights[i]);
        else {
            int cnt = 1;
            while (!signal.empty() && heights[i] > signal.top()) {
                answer[i + cnt] = i + 1;
                cnt++;
                signal.pop();
            }
            signal.push(heights[i]);
        }
    }

    return answer;
}

int main(void) {
    vector<int> heights = {1, 5, 3, 6, 7, 6, 5};

    solution(heights);

    return 0;
}