#include <bits/stdc++.h>
using namespace std;

#define ll long long

struct node {
    ll lmax=2147483647, rmax, max, sum;
    node(ll lmax, ll rmax, ll max, ll sum) : lmax(lmax), rmax(rmax), max(max), sum(sum) {};
    node() {};
};

node merge(node L, node R) {
    if (L.lmax==2147483647)
        return R;
    if (R.lmax==2147483647)
        return L;
    return node(max(L.lmax,L.sum+R.lmax),max(R.rmax,R.sum+L.rmax),max({L.max,R.max,L.rmax+R.lmax}),L.sum+R.sum);
}

ll N;

node tree[2000000];
ll lazy[2000000];

node build(ll s,ll e,ll i=1){
    if (e-s<2){
        tree[i]=node(1,1,1,1);
        return tree[i];
    }
    ll m=s+e>>1;
    tree[i]=merge(build(s,m,i<<1),build(m,e,i<<1|1));
    return tree[i];
}

void propagate(ll s,ll e,ll i=1){
    if (lazy[i]){
        if (1<e-s){
            ll m=s+e>>1;
            lazy[i<<1]=lazy[i];
            tree[i<<1].lmax=tree[i<<1].rmax=tree[i<<1].max=tree[i<<1].sum=(m-s)*lazy[i];
            lazy[i<<1|1]=lazy[i];
            tree[i<<1|1].lmax=tree[i<<1|1].rmax=tree[i<<1|1].max=tree[i<<1|1].sum=(e-m)*lazy[i];
        }
        lazy[i]=0;
    }
}

node update_lazy(ll s,ll e,ll l,ll r,ll v, ll i=1) {
    if (e<=l || r<=s) {
        propagate(s,e,i);
        return tree[i];
    }
    if (l<=s && e<=r) {
        lazy[i]=v;
        tree[i].lmax=tree[i].rmax=tree[i].max=tree[i].sum=(e-s)*v;
        return tree[i];
    }
    propagate(s,e,i);
    ll m=s+e>>1;
    tree[i]=merge(update_lazy(s,m,l,r,v,i<<1),update_lazy(m,e,l,r,v,i<<1|1));
    return tree[i];
}

node get_val(ll s,ll e,ll l,ll r,ll i=1) {
    propagate(s,e,i);
    if (e<=l || r<=s)
        return node();
    if (l<=s && e<=r)
        return tree[i];
    ll m=s+e>>1;
    return merge(get_val(s,m,l,r,i<<1),get_val(m,e,l,r,i<<1|1));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    ll M, i, j, r=0;
    cin >> N >> M;
    build(0,N);
    char Q;
    while (M){
        M--;
        cin >> Q;
        if(Q == 'A') {
            cin >> i;
            if (get_val(0,N,0,N).max<i) {
                r+=1;
                continue;
            }
            ll s=0, e=N;
            while (1<e-s) {
                ll m=s+e>>1;
                if (i<=get_val(0,N,0,m).max)
                    e=m;
                else
                    s=m;
            }
            update_lazy(0,N,e-int(i),e,-500001);
        }
        else {
            cin >> i >> j;
            update_lazy(0,N,i-1,j,1);
        }
    }
    cout<<r;
    return 0;
}