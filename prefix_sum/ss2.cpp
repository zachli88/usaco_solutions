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
    int n, x; cin >> n >> x;
    map<long long, long long> counts;
    counts[0] = 1;
    long long curr = 0;
    long long res = 0;
    for (int i = 0; i < n; ++i) {
        int num; cin >> num;
        curr += num;
        res += counts[curr - x];
        ++counts[curr];

    }
    cout << res << endl;
    return 0;
}
