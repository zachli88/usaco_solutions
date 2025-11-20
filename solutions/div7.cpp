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
    freopen("div7.in", "r", stdin);
    freopen("div7.out", "w", stdout);
    int n; cin >> n;
    int divisor = 7;
    map<int, int> remainders;
    remainders[0] = -1;
    int max_size = 0;
    int count = 0;
    for (int i = 0; i < n; ++i) {
        int curr; cin >> curr;
        count = (count + curr) % divisor;
        if (remainders.count(count) == 0) {
            remainders[count] = i;
        }
        else {
            max_size = max(max_size, i - remainders[count]);
        }
    }
    cout << max_size << endl;
    return 0;
}
