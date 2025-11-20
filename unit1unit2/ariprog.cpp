#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>  
using namespace std;

using namespace std;

int main() {
    ifstream fin("test.txt");
    ofstream fout("output.txt");

    if (!fin) {
        cerr << "Error opening input file!\n";
        return 1;
    }

    cout << "ifstream and ofstream work correctly!\n";
    return 0;
}
