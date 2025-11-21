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
    freopen("hps.in", "r", stdin);
    freopen("hps.out", "w", stdout);
    int n; cin >> n;
    int p = 0, h = 0, s = 0;
    vector<vector<int> > counts;
    for (int i = 0; i < n; ++i) {
        char c; cin >> c;
        if (c == 'P') ++p;
        else if (c == 'H') ++h;
        else ++s;
        counts.push_back(vector<int>{p, h, s});
    }
    int max_wins = 0;
    for (int i = 0; i < n - 1; ++i) {
        vector<int> diffs = {counts[counts.size() - 1][0] - counts[i][0], counts[counts.size() - 1][1] - counts[i][1], counts[counts.size() - 1][2] - counts[i][2]};
        max_wins = max(max_wins, *max_element(counts[i].begin(), counts[i].end()) + *max_element(diffs.begin(), diffs.end()));
    }
    cout << max_wins << endl;
    return 0;
}
