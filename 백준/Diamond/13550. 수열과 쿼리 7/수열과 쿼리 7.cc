#include <bits/stdc++.h>
using namespace std;

static const int tN = 1 << 20;
int tree[2 * tN];

void update(int i, int v) {
    i += tN;
    tree[i] += v;
    while (i >>= 1) {
        tree[i] = tree[i << 1] + tree[i << 1 | 1];
    }
}

int getmax() {
    if (tree[1] == 0) return 0;
    int i = 1;
    while (i < tN) {
        if (tree[i << 1 | 1]) i = i << 1 | 1;
        else i = i << 1;
    }
    return i - tN;
}

struct Query {
    int s, e, idx;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    int Q;
    cin >> Q;

    vector<Query> queries(Q);
    for (int i = 0; i < Q; i++) {
        cin >> queries[i].s >> queries[i].e;
        queries[i].idx = i;
    }

    const int blk = 400;

    vector<int> sA;
    sA.reserve(N + 1);
    sA.push_back(0);

    int cur = 0;
    for (int v : A) {
        cur = (cur + (long long)v) % K;
        sA.push_back(cur);
    }

    unordered_map<int, int> comp;

    int cid = 0;
    for (int &x : sA) {
        auto it = comp.find(x);
        if (it == comp.end()) {
            comp[x] = cid;
            x = cid;
            cid++;
        } else {
            x = it->second;
        }
    }

    vector<deque<int>> dql(cid);
    vector<int> ans(Q);

    vector<Query> ord = queries;
    sort(ord.begin(), ord.end(), [&](const Query& a, const Query& b) {
        int ab = (a.s - 1) / blk;
        int bb = (b.s - 1) / blk;
        if (ab != bb) return ab < bb;
        return a.e < b.e;
    });

    int ps = 0, pe = 0;

    for (auto &q : ord) {
        int s = q.s - 1;
        int e = q.e + 1;

        while (pe < e) {
            int v = sA[pe];
            if (!dql[v].empty()) {
                update(dql[v].back() - dql[v].front(), -1);
            }
            dql[v].push_back(pe);
            update(dql[v].back() - dql[v].front(), +1);
            pe++;
        }

        while (e < pe) {
            pe--;
            int v = sA[pe];
            update(dql[v].back() - dql[v].front(), -1);
            dql[v].pop_back();
            if (!dql[v].empty()) {
                update(dql[v].back() - dql[v].front(), +1);
            }
        }

        while (s < ps) {
            ps--;
            int v = sA[ps];
            if (!dql[v].empty()) {
                update(dql[v].back() - dql[v].front(), -1);
            }
            dql[v].push_front(ps);
            update(dql[v].back() - dql[v].front(), +1);
        }

        while (ps < s) {
            int v = sA[ps];
            update(dql[v].back() - dql[v].front(), -1);
            dql[v].pop_front();
            if (!dql[v].empty()) {
                update(dql[v].back() - dql[v].front(), +1);
            }
            ps++;
        }

        ans[q.idx] = getmax();
    }

    for (int i = 0; i < Q; i++) {
        cout << ans[i] << '\n';
    }

    return 0;
}