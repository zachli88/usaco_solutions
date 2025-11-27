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
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s; cin >> s;
    int N = s.size();
    int Q; cin >> Q;
    vector<vector<long long>> palindromes(N + 1, vector<long long>(N + 1, 0));
    for (int l = 0; l < N; ++l) {
        int l1 = l, l2 = l;
        int r1 = l, r2 = l + 1;
        while (l1 >= 0 && r1 < N && s[l1] == s[r1]) {
            palindromes[l1 + 1][r1 + 1] = 1;
            --l1;
            ++r1;
        }
        while (l2 >= 0 && r2 < N && s[l2] == s[r2]) {
            palindromes[l2 + 1][r2 + 1] = 1;
            --l2;
            ++r2;
        }
    }
    for (int r = 1; r <= N; ++r) {
        for (int c = 1; c <= N; ++c) {
            palindromes[r][c] += palindromes[r - 1][c] + palindromes[r][c - 1] - palindromes[r - 1][c - 1];
        }
    }
    for (int q = 0; q < Q; ++q) {
        int l, r; cin >> l >> r;
        int res = palindromes[r][r] - palindromes[r][l - 1] - palindromes[l - 1][r] + palindromes[l - 1][l - 1];
        cout << res << endl;
    }
    return 0;
}
