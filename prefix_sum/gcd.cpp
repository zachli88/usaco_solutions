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
    vector<long long> nums(N, 0);
    for (int i = 0; i < N; ++i) {
        cin >> nums[i];
    }
    vector<long long> left(N, 0);
    vector<long long> right(N, 0);
    left[0] = nums[0];
    right[right.size() - 1] = nums[nums.size() - 1];
    for (int i = 1; i < N; ++i) {
        left[i] = gcd(nums[i], left[i - 1]);
        right[right.size() - i - 1] = gcd(nums[nums.size() - i - 1], right[right.size() - i]);
    }
    long long res = right[1];
    for (int i = 1; i < N - 1; ++i) {
        res = max(res, gcd(left[i - 1], right[i + 1]));
    }
    res = max(res, left[left.size() - 2]);
    cout << res << endl;
    return 0;
}
