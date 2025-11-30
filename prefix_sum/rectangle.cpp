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
    int N; cin >> N;
    vector<pair<long long, int>> xValues;
    vector<pair<long long, int>> yValues;
    for (int i = 0; i < N; ++i) {
        long long x, y; cin >> x >> y;
        xValues.push_back({x, i});
        yValues.push_back({y, i});
    }
    sort(xValues.begin(), xValues.end());
    sort(yValues.begin(), yValues.end());
    vector<vector<long long>> coords(N, vector<long long>(2, 0));
    for (int i = 1; i <= N; ++i) {
        coords[xValues[i - 1].second][0] = i;
        coords[yValues[i - 1].second][1] = i;
    }
    vector<vector<long long>> prefix(N + 1, vector<long long>(N + 1, 0));
    for (int i = 0; i < N; ++i) {
        ++prefix[coords[i][0]][coords[i][1]];
    }
    for (int r = 1; r <= N; ++r) {
        for (int c = 1; c <= N; ++c) {
            prefix[r][c] += prefix[r - 1][c] + prefix[r][c - 1] - prefix[r - 1][c - 1];
        }
    }
    long long res = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            int l = min(coords[i][1], coords[j][1]), r = max(coords[i][1], coords[j][1]), t = min(coords[i][0], coords[j][0]), b = max(coords[i][0], coords[j][0]);
            int top = prefix[t][r] - prefix[t][l - 1];
            int bottom = prefix[N][r] - prefix[b - 1][r] - prefix[N][l - 1] + prefix[b - 1][l - 1];
            res += top * bottom;
        }
    }
    cout << res + N + 1 << endl;
    return 0;
}
