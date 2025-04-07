#include <vector>
#include <set>
#include <algorithm>

using namespace std;
int solution(vector<int> stones, int k) {
    multiset<int> window;
    int ans;

    for (int i = 0; i < k; ++i)
        window.insert(stones[i]);

    ans = *window.rbegin();

    for (int i = k; i < stones.size(); ++i) {
        window.insert(stones[i]);
        window.erase(window.find(stones[i - k]));
        ans = min(ans, *window.rbegin());
    }
    return ans;
}