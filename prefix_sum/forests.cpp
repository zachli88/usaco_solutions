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
    int N, Q; cin >> N >> Q;
    vector<vector<int>> prefix(N + 1, vector<int>(N + 1, 0));
    for (int r = 1; r <= N; ++r) {
        string s; cin >> s;
        for (int c = 1; c <= N; ++c) {
            prefix[r][c] = prefix[r - 1][c] + prefix[r][c - 1] - prefix[r - 1][c - 1];
            if (s[c - 1] == '*') {
                ++prefix[r][c];
            }
        }
    }
    for (int q = 0; q < Q; ++q) {
        int y1, x1, y2, x2; cin >> y1 >> x1 >> y2 >> x2;
        int res = prefix[y2][x2] - prefix[y2][x1 - 1] - prefix[y1 - 1][x2] + prefix[y1 - 1][x1 - 1];
        cout << res << endl;
    }
    return 0;
}
