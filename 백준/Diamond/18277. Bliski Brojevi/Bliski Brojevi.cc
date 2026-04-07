#include <bits/stdc++.h>
using namespace std;

const int tN = 1 << 15;
const int blk = 181;

int N, Q;
int tree[tN << 1];
int cnt[tN];
vector<int> A;

inline void update(int i, int v) {
    i += tN;
    tree[i] += v;
    while (i >>= 1) tree[i] = tree[i << 1] + tree[i << 1 | 1];
}

inline int getval(int l, int r) { // [l, r)
    l += tN;
    r += tN;
    int ret = 0;
    while (l < r) {
        if (l & 1) ret += tree[l++];
        if (r & 1) ret += tree[--r];
        l >>= 1;
        r >>= 1;
    }
    return ret;
}

inline int kth(int k) {
    int i = 1;
    while (i < tN) {
        if (tree[i << 1] > k) i <<= 1;
        else k -= tree[i << 1], i = i << 1 | 1;
    }
    return i - tN;
}

priority_queue<int, vector<int>, greater<int>> h;

inline void add_gap(int d) {
    ++cnt[d];
    h.push(d);
}

inline void del_gap(int d) {
    --cnt[d];
}

inline void push_val(int i, int v) {
    int c = getval(0, v);

    int a = 0, b = 0;
    if (c) a = kth(c - 1);
    if (c < tree[1]) b = kth(c);

    if (a && b) del_gap(b - a);
    if (a) add_gap(v - a);
    if (b) add_gap(b - v);

    update(v, 1);
}

inline void pop_val(int i, int v) {
    update(v, -1);
    int c = getval(0, v);

    int a = 0, b = 0;
    if (c) a = kth(c - 1);
    if (c < tree[1]) b = kth(c);

    if (a) del_gap(v - a);
    if (b) del_gap(b - v);
    if (a && b) add_gap(b - a);
}

struct Query {
    int l, r, idx;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> Q;
    A.resize(N);
    for (int i = 0; i < N; ++i) cin >> A[i];

    vector<Query> qs(Q);
    for (int i = 0; i < Q; ++i) {
        cin >> qs[i].l >> qs[i].r;
        --qs[i].l;
        qs[i].idx = i;
    }

    sort(qs.begin(), qs.end(), [](const Query& a, const Query& b) {
        int ab = a.l / blk, bb = b.l / blk;
        if (ab != bb) return ab < bb;
        if (ab & 1) return a.r > b.r;
        return a.r < b.r;
    });

    vector<int> ans(Q);
    int ps = 0, pe = 0;

    for (auto &q : qs) {
        int s = q.l, e = q.r;

        while (pe < e) push_val(pe, A[pe]), ++pe;
        while (ps > s) --ps, push_val(ps, A[ps]);
        while (pe > e) --pe, pop_val(pe, A[pe]);
        while (ps < s) pop_val(ps, A[ps]), ++ps;

        while (cnt[h.top()] < 1) h.pop();
        ans[q.idx] = h.top();
    }

    for (int i = 0; i < Q; ++i) cout << ans[i] << '\n';
    return 0;
}