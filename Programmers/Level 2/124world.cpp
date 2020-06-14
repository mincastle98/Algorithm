//2020.06.14
//프로그래머스 124 나라의 숫자
//정확성 100 효율성 50
//By Mincastle

#include <string>
#include <math.h>
#include <algorithm>

using namespace std;

string solution(int n) {
    string answer = "";
    int i = 1;

    while (0 < n) {
        int tmp = n % (int) pow(3, i);
        int btmp = pow(3, i - 1);

        if (tmp > 0 && tmp <= btmp)
            answer += "1";
        else if (tmp > btmp && tmp <= 2 * btmp)
            answer += "2";
        else if ((tmp > 2 * btmp && tmp < 3 * btmp) || tmp == 0)
            answer += "4";

        n -= (int) pow(3, i);
        i++;
    }
    reverse(answer.begin(), answer.end());

    return answer;
}