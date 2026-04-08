#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<vector<int>> g(N + 1), rg(N + 1);
    vector<pair<int,int>> orig;
    orig.reserve(M);

    for (int i = 0; i < M; ++i) {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        rg[v].push_back(u);
        orig.push_back({u, v});
    }

    vector<int> cash(N + 1);
    for (int i = 1; i <= N; ++i) cin >> cash[i];

    int S, P;
    cin >> S >> P;

    vector<char> is_rest_node(N + 1, 0);
    for (int i = 0; i < P; ++i) {
        int x;
        cin >> x;
        is_rest_node[x] = 1;
    }

    vector<char> vis(N + 1, 0);
    vector<int> order;
    order.reserve(N);
    vector<int> ptr(N + 1, 0);

    for (int s = 1; s <= N; ++s) {
        if (vis[s]) continue;

        stack<int> st;
        st.push(s);
        vis[s] = 1;

        while (!st.empty()) {
            int u = st.top();
            if (ptr[u] < (int)g[u].size()) {
                int v = g[u][ptr[u]++];
                if (!vis[v]) {
                    vis[v] = 1;
                    st.push(v);
                }
            } else {
                st.pop();
                order.push_back(u);
            }
        }
    }

    vector<int> comp(N + 1, -1);
    vector<long long> comp_cash;
    vector<char> comp_has_rest;
    comp_cash.reserve(N);
    comp_has_rest.reserve(N);

    int C = 0;
    stack<int> st;

    for (int i = N - 1; i >= 0; --i) {
        int s = order[i];
        if (comp[s] != -1) continue;

        comp_cash.push_back(0);
        comp_has_rest.push_back(0);

        st.push(s);
        comp[s] = C;

        while (!st.empty()) {
            int u = st.top();
            st.pop();

            comp_cash[C] += cash[u];
            if (is_rest_node[u]) comp_has_rest[C] = 1;

            for (int v : rg[u]) {
                if (comp[v] == -1) {
                    comp[v] = C;
                    st.push(v);
                }
            }
        }
        ++C;
    }

    vector<pair<int,int>> dag_edges;
    dag_edges.reserve(M);

    for (auto [u, v] : orig) {
        int cu = comp[u];
        int cv = comp[v];
        if (cu != cv) dag_edges.push_back({cu, cv});
    }

    sort(dag_edges.begin(), dag_edges.end());
    dag_edges.erase(unique(dag_edges.begin(), dag_edges.end()), dag_edges.end());

    vector<vector<int>> dag(C);
    vector<int> indeg(C, 0);

    for (auto [u, v] : dag_edges) {
        dag[u].push_back(v);
        ++indeg[v];
    }

    const long long NEG = -(1LL << 60);
    vector<long long> dp(C, NEG);

    int start_comp = comp[S];
    dp[start_comp] = comp_cash[start_comp];

    queue<int> q;
    for (int i = 0; i < C; ++i) {
        if (indeg[i] == 0) q.push(i);
    }

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : dag[u]) {
            if (dp[u] != NEG) {
                dp[v] = max(dp[v], dp[u] + comp_cash[v]);
            }
            if (--indeg[v] == 0) {
                q.push(v);
            }
        }
    }

    long long ans = 0;
    for (int i = 0; i < C; ++i) {
        if (comp_has_rest[i]) {
            ans = max(ans, dp[i]);
        }
    }

    cout << ans << '\n';
    return 0;
}