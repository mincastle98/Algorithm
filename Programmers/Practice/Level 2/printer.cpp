//2020.06.07
//프로그래머스 프린터 (큐)
//By Mincastle

#include <vector>
#include <queue>

using namespace std;

class Document {
public:
    int priority;
    int location;

    Document(int priority, int location) {
        this->priority = priority;
        this->location = location;
    }
};

int findMax(queue<Document> q) {
    int max = q.front().priority;
    while (!q.empty()) {
        if (q.front().priority > max) max = q.front().priority;
        q.pop();
    }

    return max;
}

int solution(vector<int> priorities, int location) {
    int answer = 1;
    queue<Document> nowOn;

    int size = priorities.size();
    for (int i = 0; i < size; i++) {
        nowOn.push(Document(priorities[i], i));
    }

    while (!nowOn.empty()) {
        while (nowOn.front().priority < findMax(nowOn)) {
            Document temp = nowOn.front();
            nowOn.pop();
            nowOn.push(temp);
        }

        if (nowOn.front().location == location) {
            break;
        }
        nowOn.pop();
        answer++;
    }

    return answer;
}


int main(void) {
    vector<int> priorities = {2, 1, 3, 2};

    solution(priorities, 2);

    return 0;
}

