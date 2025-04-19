#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;

    long long answer = LLONG_MAX;
    for (int i = 0; i < k; i++) {
        long long y, c1, c2;
        cin >> y >> c1 >> c2;
        long long g = gcd(c1, c2);
        long long l = c1 / g * c2;  // lcm(c1, c2)
        long long next_year = y + l;
        answer = min(answer, next_year);
    }

    cout << answer << "\n";
    return 0;
}
