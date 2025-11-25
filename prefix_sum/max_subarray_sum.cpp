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
    vector<long long> array(N, 0);
    for (int i = 0; i < N; ++i) {
        cin >> array[i];
    }
    long long min_left = 0;
    long long res = LLONG_MIN;
    long long sum = 0;
    for (int i = 0; i < N; ++i) {
        sum += array[i];
        res = max(res, sum - min_left);
        min_left = min(min_left, sum);
    }
    cout << res << endl;
    return 0;
}
