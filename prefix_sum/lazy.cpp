#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <unordered_map>
#include <map>
#include <math.h>
#include <string>
#include <climits> 
#include <set>
#include <queue>
#include <numeric>
using namespace std;

int main() {
    freopen("lazy.in", "r", stdin);
    freopen("lazy.out", "w", stdout);
    int N, K; cin >> N >> K;
    vector<vector<long long>> grass(N * 2 - 1, vector<long long>(N * 2 - 1, 0));
    for (int r = 0; r < N; ++r) {
        for (int c = 0; c < N; ++c) {
            int row = r + c;
            int col = N - 1 + c - r;
            cin >> grass[row][col];
        }
    }
    for (int r = 0; r < grass.size(); ++r) {
        for (int c = 0; c < grass.size(); ++c) {
            long long top = 0, left = 0, diagonal = 0;
            if (r > 0) top = grass[r - 1][c];
            if (c > 0) left = grass[r][c - 1];
            if (r > 0 && c > 0) diagonal = grass[r - 1][c - 1];
            grass[r][c] += top + left - diagonal;
        }
    }
    long long res = 0;
    for (int r = 0; r < grass.size(); ++r) {
        for (int c = 0; c < grass.size(); ++c) {
            long long top = 0, left = 0, diagonal = 0;
            int length = 2 * K + 1;
            if (r >= length) top = grass[r - length][c];
            if (c >= length) left = grass[r][c - length];
            if (r >= length && c >= length) diagonal = grass[r - length][c - length];
            res = max(res, grass[r][c] - top - left + diagonal);
        }
    }
    cout << res << endl;
    return 0;
}
