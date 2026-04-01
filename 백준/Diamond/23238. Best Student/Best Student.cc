#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100000;
const int MAXT = 1 << 17;
int tree[MAXT << 1];

int N, Q, blk;
int A[MAXN];

struct Query {
    int s, e, idx;
};

void update(int i, int v) {
    i += MAXT;
    tree[i] += v;
    while (i >>= 1) {
        tree[i] = max(tree[i << 1], tree[i << 1 | 1]);
    }
}

int getmax() {
    int i = 1;
    int mv = tree[1];
    while (i < MAXT) {
        if (tree[i << 1 | 1] == mv) i = i << 1 | 1;
        else i = i << 1;
    }
    return i - MAXT;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> Q;
    vector<int> raw(N);
    for (int i = 0; i < N; i++) cin >> raw[i];

    vector<Query> queries(Q);
    for (int i = 0; i < Q; i++) {
        cin >> queries[i].s >> queries[i].e;
        queries[i].idx = i;
    }

    vector<int> vals = raw;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    for (int i = 0; i < N; i++) {
        A[i] = lower_bound(vals.begin(), vals.end(), raw[i]) - vals.begin();
    }

    blk = max(1, (int)sqrt(N));

    sort(queries.begin(), queries.end(), [&](const Query& a, const Query& b) {
        int ab = (a.s - 1) / blk;
        int bb = (b.s - 1) / blk;
        if (ab != bb) return ab < bb;
        if (ab & 1) return a.e > b.e;
        return a.e < b.e;
    });

    vector<int> ans(Q);
    int ps = 0, pe = 0;

    for (const auto& qu : queries) {
        int s = qu.s - 1;
        int e = qu.e;

        while (pe < e) update(A[pe++], 1);
        while (pe > e) update(A[--pe], -1);
        while (ps < s) update(A[ps++], -1);
        while (ps > s) update(A[--ps], 1);

        int idx = getmax();
        ans[qu.idx] = vals[idx];
    }

    for (int i = 0; i < Q; i++) {
        cout << ans[i] << '\n';
    }
    return 0;
}