#include <iostream>
using namespace std;
#define endl '\n'

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int K;
    string P;
    cin >> P >> K;
    cout << P << endl;
    int ret = 0;
    for(int j = 0; j <P.size(); j++){
        ret = (ret * 10 + P[j] - '0');
        cout << ret << endl;
    }
    // bool is_BAD = false;
    // for(int i = 2; i <= K; i++){
    //     if (P % i == 0) {
    //         cout << "BAD" << " " << i << endl;
    //         is_BAD = true;
    //         break;
    //     }
    // }
    // if (!is_BAD) cout << "GOOD" << endl;
    return 0;
}