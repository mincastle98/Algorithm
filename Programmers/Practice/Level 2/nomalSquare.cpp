//2020.06.18
//프로그래머스 멀쩡한 사각형 (Summer/Winter Coding(2019))
//By Mincastle

using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int tmp = a % b;
        a = b;
        b = tmp;
    }
    return a;
}

long long solution(int w, int h) {
    long long answer;
    int cnt = gcd(w, h);
    int w_ = w / cnt;
    int h_ = h / cnt;

    int box = w_ + h_ - 1;
    answer = (long) w * h - box * cnt;

    return answer;
}

int main(void) {
    solution(8, 12);

    return 0;
}