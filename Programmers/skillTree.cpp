//2020.06.07
//프로그래머스 스킬트리 (Summer/Winter Coding(~2018))
//By Mincastle

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    vector<char> pre_skill;
    for (int i = 0; i < skill.length(); i++) {
        pre_skill.push_back(skill[i]);
    }
    reverse(pre_skill.begin(), pre_skill.end());

    for (int i = 0; i < skill_trees.size(); i++) {
        bool isPossible = true;
        vector<char> temp = pre_skill;

        for (int j = 0; j < skill_trees[i].size(); j++) {
            if (find(pre_skill.begin(), pre_skill.end(), skill_trees[i][j]) != pre_skill.end()) {
                if (skill_trees[i][j] == temp.back()) {
                    temp.pop_back();
                } else {
                    isPossible = false;
                    break;
                }
            }
        }
        if (isPossible) answer++;
    }

    return answer;
}


int main(void) {
    string skill = "CBD";
    vector<string> skill_trees = {"BACDE", "CBADF", "AECB", "BDA"};

    solution(skill, skill_trees);

    return 0;
}
