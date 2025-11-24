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
    for (int t = 0; t < T; ++t) {
        int N; cin >> N;
        vector<long long> nums(N, 0);
        for (int i = 0; i < N; ++i) {
            cin >> nums[i];
        }
        vector<long long> prefix(N, 0);
        vector<long long> suffix(N, 0);
        prefix[0] = nums[0];
        suffix[N - 1] = nums[N - 1] - (N - 1);
        for (int i = 1; i < N; ++i) {
            prefix[i] = max(prefix[i - 1], nums[i] + i);
        }
        for (int i = N - 2; i >= 0; --i) {
            suffix[i] = max(suffix[i + 1], nums[i] - i);
        }
        long long res = INT32_MIN;
        for (int i = 1; i < N - 1; ++i) {
            res = max(res, nums[i] + prefix[i - 1] + suffix[i + 1]);
        }
        cout << res << endl;
    }
    return 0;
}
