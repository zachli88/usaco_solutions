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
    int N, M, Q; cin >> N >> M >> Q;
    vector<vector<int>> grid(N + 1, vector<int>(M + 1, 0));
    for (int n = 1; n <= N; ++n) {
        for (int m = 1; m <= M; ++m) {
            char c; cin >> c;
            if (c == '1') {
                grid[n][m] = 1;
            }
        }
    }
    vector<vector<int>> prefix(N + 1, vector<int>(M + 1, 0));
    for (int r = 1; r <= N; ++r) {
        for (int c = 1; c <= M; ++c) {
            prefix[r][c] = prefix[r - 1][c] + prefix[r][c - 1] - prefix[r - 1][c - 1];
            if (grid[r][c] == 1) {
                if (grid[r - 1][c] == 1 && grid[r][c - 1] == 1) {
                    --prefix[r][c];
                }
                if (grid[r - 1][c] == 0 && grid[r][c - 1] == 0) {
                    ++prefix[r][c];
                }
            }
        }
    }
    vector<vector<int>> row_prefix(N + 1, vector<int>(M + 1, 0));
    vector<vector<int>> col_prefix(N + 1, vector<int>(M + 1, 0));
    for (int r = 1; r <= N; ++r) {
        for (int c = 1; c <= M; ++c) {
            row_prefix[r][c] = row_prefix[r][c - 1];
            col_prefix[r][c] = col_prefix[r - 1][c];
            if (grid[r][c] == 1) {
                if (grid[r - 1][c] == 0) {
                    ++col_prefix[r][c];
                }
                if (grid[r][c - 1] == 0) {
                    ++row_prefix[r][c];
                }
            }
        }
    }
    
    for (int q = 0; q < Q; ++q) {
        int x1, y1, x2, y2; cin >> x1 >> y1 >> x2 >> y2;
        int res = prefix[x2][y2] - prefix[x2][y1] - prefix[x1][y2] + prefix[x1][y1];
        res += row_prefix[x1][y2] - row_prefix[x1][y1] + col_prefix[x2][y1] - col_prefix[x1][y1];
        if (grid[x1][y1]) {
            res += 1;
        }
        cout << res << endl;
    }
}
