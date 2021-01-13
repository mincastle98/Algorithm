//2020.06.27
//프로그래머스 카카오프렌즈 컬러링북 (2017 카카오코드 예선)
//By Mincastle

#include <vector>
#include <algorithm>

using namespace std;

int areaCnt;

vector<vector<int>> checkArea(int m, int n, vector<vector<int>> picture, vector<vector<int>> visited) {
    visited[m][n] = areaCnt;

    if (m != 0 && visited[m - 1][n] == 0 && picture[m][n] == picture[m - 1][n])
        visited = checkArea(m - 1, n, picture, visited);
    if (n != 0 && visited[m][n - 1] == 0 && picture[m][n] == picture[m][n - 1])
        visited = checkArea(m, n - 1, picture, visited);
    if (m != picture.size() - 1 && visited[m + 1][n] == 0 && picture[m][n] == picture[m + 1][n])
        visited = checkArea(m + 1, n, picture, visited);
    if (n != picture[0].size() - 1 && visited[m][n + 1] == 0 && picture[m][n] == picture[m][n + 1])
        visited = checkArea(m, n + 1, picture, visited);

    return visited;
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;

    vector<vector<int>> visited(m);
    vector<int> tmp(n, 0);
    for (int i = 0; i < m; i++) {
        visited[i] = tmp;
    }
    areaCnt = 1;

    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            if (visited[i][j] == 0 && picture[i][j] != 0) {
                visited = checkArea(i, j, picture, visited);
                areaCnt++;
            }
        }


    vector<int> check(--areaCnt, 0);
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            if (visited[i][j] != 0)
                check[visited[i][j] - 1]++;

    number_of_area = areaCnt;
    max_size_of_one_area = *max_element(check.begin(), check.end());

    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;

    return answer;
}

int main(void) {
    vector<vector<int>> picture = {{1, 1, 1, 0},
                                   {1, 2, 2, 0},
                                   {1, 0, 0, 1},
                                   {0, 0, 0, 1},
                                   {0, 0, 0, 3},
                                   {0, 0, 0, 3}};
    solution(6, 4, picture);

    return 0;
}
