#include <iostream>
#include <algorithm>
using namespace std;

#define ll long long

struct node {
  ll max, min, AB, BC, ABC;
  node(ll max=-922337203685477580, ll min=922337203685477580, ll AB=-922337203685477580, ll BC=-922337203685477580, ll ABC=-922337203685477580) :max(max),min(min),AB(AB),BC(BC),ABC(ABC) {};
};

int N,Q,t,q,i,j;

node tree[666666];

node merge(node &L, node &R){
  return node(max(L.max,R.max),min(L.min,R.min),max({L.AB,R.AB,R.max-L.min}),max({L.BC,R.BC,L.max-R.min}),max({L.ABC,R.ABC,L.AB-R.min,R.BC-L.min}));
}

void update(int i, int v){
  i+=N;
  tree[i]=node(v,v);
  while (1<i){
    i>>=1;
    tree[i]=merge(tree[i*2],tree[i*2|1]);
  }
}

ll getval(int l, int r){
  l+=N;
  r+=N;
  node right,left;
  while(l<r){
    if(l&1){
      left=merge(left,tree[l]);
      l++;
    }
    if(r&1){
      r--;
      right=merge(tree[r],right);
    }
    l>>=1;
    r>>=1;
  }
  return merge(left,right).ABC;
}

int main(){
  cin.tie(0);
  cout.tie(0);
  ios_base::sync_with_stdio(false);
  cin>>N>>Q;
  for(int i=0;i<N;i++){
    cin>>t;
    tree[i+N]=node(t,t);
  }
  for(int i=N-1;0<i;i--){
    tree[i]=merge(tree[i*2],tree[i*2|1]);
  }
  while(Q){
    Q--;
    cin>>q>>i>>j;
    if(q-1)
      cout<<getval(i-1,j)<<"\n";
    else
      update(i-1,j);
  }
}