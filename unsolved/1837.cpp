#include <iostream>
using namespace std;
#define endl '\n'

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int P, K;
    cin >> P >> K;

    bool is_BAD = false;
    for(int i = 2; i < K; i++){
        if (P % i == 0) {
            cout << "BAD" << " " << i << endl;
            is_BAD = true;
            break;
        }
    }
    if (!is_BAD) cout << "GOOD" << endl;
    return 0;
}