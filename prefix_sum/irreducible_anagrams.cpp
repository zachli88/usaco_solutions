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
    string s; cin >> s;
    vector<vector<int>> counts(s.size() + 1, vector<int>());
    counts[0] = vector<int>(26, 0);
    for (int i = 1; i <= s.size(); ++i) {
        counts[i] = counts[i - 1];
        ++counts[i][s[i - 1] - 'a'];
    }
    int Q; cin >> Q;
    for (int q = 0; q < Q; ++q) {
        int l, r; cin >> l >> r;
        int diffs = 0;
        for (int i = 0; i < 26; ++i) {
            if (counts[r][i] - counts[l - 1][i] > 0) {
                ++diffs;
            }
        }
        if (diffs >= 3 || s[r - 1] != s[l - 1] || l == r) {
            cout << "Yes" << endl;
        }
        else {
            cout << "No" << endl;
        }
    }
    return 0;
}
