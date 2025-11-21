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
    int T; cin >> T;
    for (int i = 0; i < T; ++i) {
        int N; cin >> N;
        map<long long, long long> counts({{0, 1}});
        long long total = 0;
        long long res = 0;
        for (int j = 0; j < N; ++j) {
            char c; cin >> c;
            total += c - '0' - 1;
            res += counts[total];
            ++counts[total];
        }
        cout << res << endl;
    }
    return 0;
}
