#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll NEG = -(1LL << 60);

struct node {
    ll n[4][4];
    int len;

    node() {
        len = 0;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                n[i][j] = NEG;
    }

    node(ll v) {
        len = 1;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                n[i][j] = NEG;
        n[0][0] = 0;
        n[1][1] = v;
    }
};

int N, Q;
vector<node> tree;

node merge_node(const node& L, const node& R) {
    if (L.len == 0) return R;
    if (R.len == 0) return L;

    node ret;
    ret.len = L.len + R.len;

    for (int a = 0; a < 4; a++) {
        for (int b = 0; b < 4; b++) {
            if (L.n[a][b] == NEG) continue;
            for (int c = 0; c < 4; c++) {
                if (3 < b + c) continue;
                for (int d = 0; d < 4; d++) {
                    if (R.n[c][d] == NEG) continue;

                    ll val = L.n[a][b] + R.n[c][d];

                    int na = a;
                    if (L.len < 4 && a == L.len)
                        na += c;

                    int nd = d;
                    if (R.len < 4 && d == R.len)
                        nd += b;

                    ret.n[na][nd] = max(ret.n[na][nd], val);
                }
            }
        }
    }

    return ret;
}

void update(int i, ll v) {
    i += N;
    tree[i] = node(v);
    while (i >>= 1) {
        tree[i] = merge_node(tree[i << 1], tree[i << 1 | 1]);
    }
}

node getval(int l, int r) {
    l += N;
    r += N;
    node left, right;

    while (l < r) {
        if (l & 1) {
            left = merge_node(left, tree[l]);
            l++;
        }
        if (r & 1) {
            --r;
            right = merge_node(tree[r], right);
        }
        l >>= 1;
        r >>= 1;
    }
    return merge_node(left, right);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    vector<ll> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];

    tree.assign(2 * N, node());

    for (int i = 0; i < N; i++) {
        tree[N + i] = node(A[i]);
    }

    for (int i = N - 1; i > 0; i--) {
        tree[i] = merge_node(tree[i << 1], tree[i << 1 | 1]);
    }

    auto print_answer = [&]() {
        node cur = getval(0, N);
        ll ans = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (i + j < 4) ans = max(ans, cur.n[i][j]);
            }
        }
        cout << ans << '\n';
    };

    print_answer();

    cin >> Q;
    while (Q--) {
        int p;
        ll v;
        cin >> p >> v;
        update(p - 1, v);
        print_answer();
    }

    return 0;
}