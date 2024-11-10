#include <iostream>
#include <vector>
using namespace std;

int N, K;
vector<int> l;
vector<int> tree;

// Function to build the segment tree
int build(int start, int end, int idx = 1) {
    if (end - start == 1) {
        tree[idx] = l[start];
        return tree[idx];
    }
    int mid = (start + end) / 2;
    tree[idx] = build(start, mid, idx * 2) | build(mid, end, idx * 2 + 1);
    return tree[idx];
}

// Function to get the value in a specific range
int get_val(int start, int end, int left, int right, int idx = 1) {
    if (end <= left || right <= start) {
        return 0;
    }
    if (left <= start && end <= right) {
        return tree[idx];
    }
    int mid = (start + end) / 2;
    return get_val(start, mid, left, right, idx * 2) | get_val(mid, end, left, right, idx * 2 + 1);
}

// Function to find the right boundary using binary search
int bisect_right(int start) {
    int s = start + 1, e = N + 1;
    while (e - s > 1) {
        int m = (s + e) / 2;
        if (K < get_val(0, N, start, m)) {
            e = m;
        } else {
            s = m;
        }
    }
    if (get_val(0, N, start, s) == K) {
        return s;
    }
    return -1;
}

// Function to find the left boundary using binary search
int bisect_left(int start) {
    int s = start, e = N;
    while (e - s > 1) {
        int m = (s + e) / 2;
        if (K <= get_val(0, N, start, m)) {
            e = m;
        } else {
            s = m;
        }
    }
    if (get_val(0, N, start, e) == K) {
        return e;
    }
    return -1;
}

// Function to get the interval length
int get_interval(int start) {
    int start_pos = bisect_left(start);
    if (start_pos < 0) {
        return 0;
    }
    int end_pos = bisect_right(start);
    return end_pos - start_pos + 1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> N >> K;
    l.resize(N);
    tree.resize(N * 4);

    for (int i = 0; i < N; ++i) {
        cin >> l[i];
    }

    build(0, N);

    long long result = 0;
    for (int i = 0; i < N; ++i) {
        result += get_interval(i);
    }
    cout << result << endl;

    return 0;
}