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
    int N, M; cin >> N >> M;
    vector<long long> salt(N, 0);
    for (int i = 0; i < N; ++i) {
        cin >> salt[i];
    }
    for (int i = 1; i < N; ++i) {
        salt[i] = max(salt[i], salt[i - 1] - M);
    }
    for (int i = N - 2; i >= 0; --i) {
        salt[i] = max(salt[i], salt[i + 1] - M);
    }
    for (int i = 0; i < N; ++i) {
        cout << salt[i] << " ";
    }
    cout << endl;
    return 0;
}
