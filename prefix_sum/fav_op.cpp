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
        int N, M; cin >> N >> M;
        vector<long long> nums;
        for (int i = 0; i < N; ++i) {
            int num; cin >> num;
            nums.push_back(num % M);
        }
        sort(nums.begin(), nums.end());
        for (long long i = 0; i < N; ++i) {
            nums.push_back(nums[i] + M);
        }
        vector<long long> prefix(2 * N + 1, 0);
        for (long long i = 1; i < prefix.size(); ++i) {
            prefix[i] = prefix[i - 1] + nums[i - 1];
        }
        long long res = LLONG_MAX;;
        for (long long i = N; i < prefix.size(); ++i) {
            res = min(res, (prefix[i] - prefix[i - N / 2]) - (prefix[i - (N + 1) / 2] - prefix[i - N]));
        }
        cout << res << endl;
    }
    return 0;
    // 0 1 2 3 4 5 6 7 8 9 10
}
