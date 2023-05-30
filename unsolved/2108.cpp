#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
#define endl '\n'

int main(){
    int N;
    cin >> N;
    int nums[N];
    int sum = 0;
    for(int i = 0; i < N; i++){
        cin >> nums[i];
        sum += nums[i];
    }
    sort(nums, nums+N);
    cout << floor(sum / N + 0.5) << endl;
    cout << nums[(N-1)/2];

    return 0;
}