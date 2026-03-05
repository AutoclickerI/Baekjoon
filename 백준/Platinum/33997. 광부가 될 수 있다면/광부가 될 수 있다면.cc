#include <bits/stdc++.h>
using namespace std;

#define ll long long

struct node {
    ll lmax=9223372036854775807, lmaxt, rmax, rmaxt, maxt, sum, sumt;
    node(ll lmax, ll lmaxt, ll rmax, ll rmaxt, ll maxt, ll sum, ll sumt) : lmax(lmax), lmaxt(lmaxt), rmax(rmax), rmaxt(rmaxt), maxt(maxt), sum(sum), sumt(sumt) {};
    node() {};
};

node merge(node L, node R) {
    if (L.lmax==9223372036854775807)
        return R;
    if (R.lmax==9223372036854775807)
        return L;
    return node(max(L.lmax,L.sum+R.lmax),
                max({L.lmaxt,L.sum+R.lmaxt,L.sumt+R.lmax}),
                max(R.rmax,R.sum+L.rmax),
                max({R.rmaxt,R.sum+L.rmaxt,R.sumt+L.rmax}),
                max({L.maxt,R.maxt,L.rmax+R.lmaxt,L.rmaxt+R.lmax}),
                L.sum+R.sum,
                max(L.sumt+R.sum,L.sum+R.sumt));
}

ll N, M;

node tree[2000];

void update(ll i, ll v) {
    i+=N;
    ll k=tree[i].sum, t=tree[i].sumt;
    tree[i]=node(v+k,v+t,v+k,v+t,v+t,v+k,v+t);
    while (i=i>>1)
        tree[i]=merge(tree[i<<1],tree[i<<1|1]);
}

node get_val(ll l, ll r) {
    l+=N;
    r+=N;
    node right, left;
    while (l<r){
        if (l&1) {
            left=merge(left,tree[l]);
            l++;
        }
        if (r&1) {
            r--;
            right=merge(tree[r],right);
        }
        l>>=1;
        r>>=1;
    }
    return merge(left,right);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin >> M >> N;
    vector<ll> r(N,0);
    while (M){
        M--;
        ll v;
        for (ll i=0;i<N;i++) {
            cin>>v;
            tree[i+N]=node(v,v+r[i],v,v+r[i],v+r[i],v,v+r[i]);
        }
        for (ll i=N-1;0<i;i--)
            tree[i]=merge(tree[i<<1],tree[i<<1|1]);
        for (ll i=0;i<N;i++) {
            update(i,1000000000000000000);
            r[i]=get_val(0,N).maxt-1000000000000000000;
            update(i,-1000000000000000000);
        }
    }
    ll rr=r[0];
    for (auto& v : r) {
        rr=max(rr,v);
    }
    cout<<rr;
    return 0;
}