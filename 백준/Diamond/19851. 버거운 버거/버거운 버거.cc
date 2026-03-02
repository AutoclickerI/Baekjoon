#include <bits/stdc++.h>
using namespace std;

struct node {
    int min=2147483647;
    int max;
    int sum;
    node(int min, int max, int sum) : min(min), max(max), sum(sum) {}
    node() {};
};

node merge(node L, node R) {
    if (L.min==2147483647)
        return R;
    if (R.min==2147483647)
        return L;
    return node(min(L.min,L.sum+R.min),max(L.max,L.sum+R.max),L.sum+R.sum);
}

int N;
string ss;

node tree[4000000];
int lazy[4000000];

node build(int s,int e,int i=1){
    if (e-s<2){
        int v=-((int)('('<ss[s]))|1;
        tree[i]=node(min(v,0),max(v,0),v);
        return tree[i];
    }
    int m=s+e>>1;
    tree[i]=merge(build(s,m,i<<1),build(m,e,i<<1|1));
    return tree[i];
}

void propagate(int s,int e,int i=1){
    if (lazy[i]){
        if (1<e-s){
            lazy[i<<1]^=1;
            tree[i<<1]=node(-tree[i<<1].max,-tree[i<<1].min,-tree[i<<1].sum);
            lazy[i<<1|1]^=1;
            tree[i<<1|1]=node(-tree[i<<1|1].max,-tree[i<<1|1].min,-tree[i<<1|1].sum);
        }
        lazy[i]=0;
    }
}

node update_lazy(int s,int e,int l,int r,int i=1) {
    if (e<=l || r<=s) {
        propagate(s,e,i);
        return tree[i];
    }
    if (l<=s && e<=r) {
        lazy[i]^=1;
        tree[i]=node(-tree[i].max,-tree[i].min,-tree[i].sum);
        return tree[i];
    }
    propagate(s,e,i);
    int m=s+e>>1;
    tree[i]=merge(update_lazy(s,m,l,r,i<<1),update_lazy(m,e,l,r,i<<1|1));
    return tree[i];
}

node get_val(int s,int e,int l,int r,int i=1) {
    propagate(s,e,i);
    if (e<=l || r<=s)
        return node();
    if (l<=s && e<=r)
        return tree[i];
    int m=s+e>>1;
    return merge(get_val(s,m,l,r,i<<1),get_val(m,e,l,r,i<<1|1));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cin >> N;
    cin >> ss;
    build(0,N);
    int Q,q,i,j;
    cin >> Q;
    while (Q){
        Q--;
        cin>>q>>i>>j;
        if(q<2)
            update_lazy(0,N,i-1,j);
        else {
            node n=get_val(0,N,i-1,j);
            cout<<j-i+1+n.sum-n.min*2<<'\n';
        }
    }
    return 0;
}