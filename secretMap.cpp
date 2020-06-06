//2020.06.05
//프로그래머스 비밀지도 (2018 KAKAO BLIND RECRUITMENT)

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    vector<int> temp = arr1;

    for (int i = 0; i < arr2.size(); i++) {
        temp[i] = arr1[i] | arr2[i];
    }

    for (int i = 0; i < n; i++) {
        int cnt = n;

        answer.push_back("");
        while (temp[i]) {
            temp[i] & 1 ? answer[i].append("#") : answer[i].append(" ");
            temp[i] /= 2;
            cnt--;
        }

        for (int j = 0; j < cnt; j++) {
            answer[i].append(" ");
        }
        reverse(answer[i].begin(), answer[i].end());
    }

    return answer;
}

int main(void) {
    vector<int> arr1 = {9, 20, 28, 18, 11};
    vector<int> arr2 = {30, 1, 21, 17, 28};

    solution(5, arr1, arr2);

    return 0;
}