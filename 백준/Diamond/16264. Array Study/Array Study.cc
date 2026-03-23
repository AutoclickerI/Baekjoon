#include <bits/stdc++.h>
using namespace std;

static constexpr int tN = 131072;

vector<int> tree(2 * tN, 0);
vector<deque<int>> dql(200002);

void update(int i, int v) {
    i += tN;
    tree[i] += v;
    while (i >>= 1) {
        tree[i] = tree[i << 1] + tree[i << 1 | 1];
    }
}

int getmax() {
    int i = 1;
    while (i < tN) {
        if (tree[i << 1 | 1]) i = i << 1 | 1;
        else i = i << 1;
    }
    return i - tN;
}

struct Query {
    int s, e;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        vector<int> A(N);
        for (int i = 0; i < N; ++i) cin >> A[i];

        int Q;
        cin >> Q;
        vector<Query> l(Q);
        for (int i = 0; i < Q; ++i) {
            cin >> l[i].s >> l[i].e;
        }

        int blk = 700;

        vector<int> sA(N + 1, 0);
        for (int i = 0; i < N; ++i) {
            sA[i + 1] = sA[i] + A[i];
        }

        sort(l.begin(), l.end(), [&](const Query& a, const Query& b) {
            if (a.s / blk != b.s / blk) return a.s / blk < b.s / blk;
            return a.e < b.e;
        });

        l.push_back({N + 2, N});  // sentinel

        int ps = 0, pe = 0;
        long long r = 0;

        for (auto [s0, e0] : l) {
            int s = s0 - 1;
            int e = e0 + 1;

            while (pe < e) {
                int x = sA[pe] + 100001;
                if (!dql[x].empty()) {
                    update(dql[x].back() - dql[x].front(), -1);
                }
                dql[x].push_back(pe);
                update(dql[x].back() - dql[x].front(), 1);
                ++pe;
            }

            while (e < pe) {
                --pe;
                int x = sA[pe] + 100001;
                update(dql[x].back() - dql[x].front(), -1);
                dql[x].pop_back();
                if (!dql[x].empty()) {
                    update(dql[x].back() - dql[x].front(), 1);
                }
            }

            while (s < ps) {
                --ps;
                int x = sA[ps] + 100001;
                if (!dql[x].empty()) {
                    update(dql[x].back() - dql[x].front(), -1);
                }
                dql[x].push_front(ps);
                update(dql[x].back() - dql[x].front(), 1);
            }

            while (ps < s) {
                int x = sA[ps] + 100001;
                update(dql[x].back() - dql[x].front(), -1);
                dql[x].pop_front();
                if (!dql[x].empty()) {
                    update(dql[x].back() - dql[x].front(), 1);
                }
                ++ps;
            }

            r += getmax();
        }

        cout << r << '\n';
    }

    return 0;
}