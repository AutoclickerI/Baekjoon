#include <vector>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> stones, int k) {
    multiset<int> window;
    int ans;

    // Insert the first k elements into the multiset
    for (int i = 0; i < k; ++i) {
        window.insert(stones[i]);
    }

    // Initialize ans with the maximum element in the multiset
    ans = *window.rbegin();

    // Slide the window through the stones array
    for (int i = k; i < stones.size(); ++i) {
        window.insert(stones[i]);                  // Insert new element
        window.erase(window.find(stones[i - k]));  // Remove the element that's no longer in the window
        ans = min(ans, *window.rbegin());          // Update ans with the minimum of ans and current max
    }

    return ans;
}