//2020.06.06
//프로그래머스 다트게임 (2018 KAKAO BLIND RECRUITMENT)
//By Mincastle

#include <string>
#include <vector>
#include <math.h>

using namespace std;

int solution(string dartResult) {
    int answer = 0;
    vector<int> temp_score;

    char temp_;
    while (!dartResult.empty()) {
        char temp = dartResult[0];
        if (isdigit(dartResult[0])) {
            if (!temp_score.empty() && isdigit(temp_)) {
                temp_score.back() *= 10;
                temp_score.back() += temp - 48;
            } else temp_score.push_back(temp - 48);
        } else if (isalpha(dartResult[0])) {
            if (temp == 'D') temp_score.back() = pow(temp_score.back(), 2);
            else if (temp == 'T') temp_score.back() = pow(temp_score.back(), 3);
        } else if (dartResult[0] == '*') {
            temp_score.back() *= 2;
            if (temp_score.size() != 1)
                temp_score[temp_score.size() - 2] *= 2;
        } else if (dartResult[0] == '#') {
            temp_score.back() *= -1;
        }

        dartResult = dartResult.substr(1);
        temp_ = temp;
    }

    for (int i = 0; i < temp_score.size(); i++) {
        answer += temp_score[i];
    }

    return answer;
}

int main(void) {
    string dartResult = "1S2D*3T";

    solution(dartResult);

    return 0;
}
