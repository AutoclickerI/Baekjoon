#include <bits/stdc++.h>
using namespace std;

#define ll long long

struct node {
    ll lmaxp=9223372036854775807,lmaxv,lmaxpv,lmaxvp,rmaxp,rmaxv,rmaxpv,rmaxvp,sump,sumv,sumpv,sumvp,max;
    node(ll lmaxp,ll lmaxv,ll lmaxpv,ll lmaxvp,ll rmaxp,ll rmaxv,ll rmaxpv,ll rmaxvp,ll sump,ll sumv,ll sumpv,ll sumvp,ll max):lmaxp(lmaxp),lmaxv(lmaxv),lmaxpv(lmaxpv),lmaxvp(lmaxvp),rmaxp(rmaxp),rmaxv(rmaxv),rmaxpv(rmaxpv),rmaxvp(rmaxvp),sump(sump),sumv(sumv),sumpv(sumpv),sumvp(sumvp),max(max){};
    node() {};
};

node merge(node L, node R) {
    if (L.lmaxp==9223372036854775807)
        return R;
    if (R.lmaxp==9223372036854775807)
        return L;
    return node(max(L.lmaxp,L.sump+R.lmaxp),
                max(L.lmaxv,L.sumv+R.lmaxv),
                max({L.lmaxpv,L.sumpv+R.lmaxv,L.sump+R.lmaxpv}),
                max({L.lmaxvp,L.sumvp+R.lmaxp,L.sumv+R.lmaxvp}),
                max(R.rmaxp,R.sump+L.rmaxp),
                max(R.rmaxv,R.sumv+L.rmaxv),
                max({R.rmaxpv,R.sumpv+L.rmaxp,R.sumv+L.rmaxpv}),
                max({R.rmaxvp,R.sumvp+L.rmaxv,R.sump+L.rmaxvp}),
                L.sump+R.sump,
                L.sumv+R.sumv,
                max(L.sump+R.sumpv,L.sumpv+R.sumv),
                max(L.sumv+R.sumvp,L.sumvp+R.sump),
                max({L.max,R.max,L.rmaxvp+R.lmaxp,L.rmaxv+R.lmaxvp,L.rmaxpv+R.lmaxv,L.rmaxp+R.lmaxpv})
                );
}

ll N;

node tree[4000];

void update(ll i,ll p,ll v) {
    i+=N;
    tree[i]=node(node(p,v,p,v,p,v,v,p,p,v,max(p,v),max(p,v),max(p,v)));
    while (i=i>>1)
        tree[i]=merge(tree[i<<1],tree[i<<1|1]);
}

ll getval(ll l,ll r) {
    l+=N;
    r+=N;
    node right, left;
    while (l<r) {
        if (l&1)
            left=merge(left,tree[l++]);
        if (r&1)
            right=merge(tree[--r],right);
        l>>=1;
        r>>=1;
    }
    return merge(left,right).max;
}

ll max_path(vector<array<ll,4>> arr) {
    vector<ll> xs;
    for (auto &a : arr) xs.push_back(a[1]);
    sort(xs.begin(), xs.end());
    xs.erase(unique(xs.begin(), xs.end()), xs.end());
    N=xs.size();
    vector<array<ll,4>> l;
    for (auto &a : arr) {
        ll cx = lower_bound(xs.begin(), xs.end(), a[1]) - xs.begin();
        l.push_back({a[0], cx, a[2], a[3]});
    }
    sort(l.begin(), l.end());
    vector<vector<array<ll,4>>> t;
    for (auto& qq : l) {
        ll i=qq[0],j=qq[1],k=qq[2],p=qq[3];
        if (t.begin()!=t.end() && t[t.size()-1][0][0]==i)
            t[t.size()-1].push_back({i,j,k,p});
        else
            t.push_back(vector<array<ll,4>>({{i,j,k,p}}));
    }
    ll m=0;
    for (int i=0;i<t.size();i++) {
        for (int j=0;j<2*N;j++)
            tree[j].lmaxp=9223372036854775807;
        for (int j=i;j<t.size();j++) {
            for (auto& qq : t[j])
                update(qq[1],qq[2],qq[3]);
            m=max(m,getval(0,N));
        }
    }
    return m;
}

vector<array<ll,4>> swapxy(vector<array<ll,4>> arr) {
    vector<array<ll,4>> ret;
    for (auto& [y,x,p,v]:arr)
        ret.push_back({x,y,p,v});
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin>>N;
    vector<array<ll,4>> arr;
    while(N--){
        ll y,x,p,v;
        cin>>y>>x>>p>>v;
        arr.push_back({y,x,p,v});
    }
    cout<<max(max_path(arr),max_path(swapxy(arr)));
    return 0;
}