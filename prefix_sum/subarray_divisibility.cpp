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
    int n; cin >> n;
    map<long long, long long> counts;
    counts[0] = 1;
    long long curr = 0;
    long long res = 0;
    for (int i = 0; i < n; ++i) {
        long long num; cin >> num;
        curr = (((curr + num) % n) + n) % n;
        res += counts[curr];
        ++counts[curr];

    }
    cout << res << endl;
    return 0;
}
