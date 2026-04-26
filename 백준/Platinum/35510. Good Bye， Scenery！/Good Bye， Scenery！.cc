#include <bits/stdc++.h>
using namespace std;

#define ll long long

struct node {
  ll sum, max;
  node(ll sum=0, ll max=0):sum(sum),max(max) {}
};

int N;
node tree[600005];

node merge(const node &L, const node &R){
  return node(L.sum+R.sum, max(L.max,R.max));
}

void update(int i, int mx, int s){
  i+=N;
  tree[i]=node(s,mx);
  while(1<i){
    i>>=1;
    tree[i]=merge(tree[i<<1],tree[i<<1|1]);
  }
}

node getval(int l, int r){
  l+=N;
  r+=N;
  node ret;
  while(l<r){
    if(l&1){
      ret=merge(ret,tree[l]);
      l++;
    }
    if(r&1){
      r--;
      ret=merge(tree[r],ret);
    }
    l>>=1;
    r>>=1;
  }
  return ret;
}

int main(){
  cin.tie(0);
  cout.tie(0);
  ios_base::sync_with_stdio(false);

  int T;
  cin>>T;

  while(T--){
    int n,v,x;
    cin>>n;

    N=n+1;

    vector<vector<int>> B(N);

    for(int i=0;i<N;i++)
      tree[N+i]=node(i>0,0);

    for(int i=1;i<=n;i++){
      cin>>v;
      B[v].push_back(i);
    }

    for(int i=N-1;0<i;i--)
      tree[i]=merge(tree[i<<1],tree[i<<1|1]);

    ll ans=0;
    bool chk=1;

    for(int p=n;0<p;p--){
      for(auto &i:B[p])
        update(i,i,1);

      x=getval(1,n+1).max;

      if(x<1){
        chk=0;
        break;
      }

      ans+=getval(x+1,n+1).sum;
      update(x,0,0);
    }

    cout<<(chk?ans:-1)<<'\n';
  }
}