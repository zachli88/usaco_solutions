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
    freopen("maxcross.in", "r", stdin);
    freopen("maxcross.out", "w", stdout);
    int N, K, B; cin >> N >> K >> B;
    vector<int> counts(N + 1, 0);
    set<int> broken;
    for (int i = 0; i < B; ++i) {
        int b; cin >> b;
        broken.insert(b);
    }

    int count = 0;
    for (int i = 0; i <= N; ++i) {
        if (broken.count(i) == 0) {
            ++count;
        }
        counts[i] = count;
    }

    int minLights = INT32_MAX;
    for (int i = K; i <= N; ++i) {
        int workingLights = counts[i] - counts[i - K];
        minLights = min(minLights, K - workingLights);
    }

    cout << minLights << endl;
    return 0;
}
