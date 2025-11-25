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
    map<int, long long> freqs{{0, 1}};
    int curr = 0;
    int pow = 1;
    int MOD = 2019;
    long long res = 0;
    for (int i = s.size() - 1; i >= 0; --i) {
        int digit = s[i] - '0';
        curr = (curr + digit * pow) % MOD;
        pow = (pow * 10) % 2019;
        res += freqs[curr];
        ++freqs[curr];
    }
    cout << res << endl;
    return 0;
}
