from heapq import*
h=heappush
p=heappop
_,*x=map(int,open(0).read().split())
while x:S=[];L=[];a=[];exec('i^=1;h(L,x.pop(0));h(S,-p(L))\nif i:h(L,-p(S));a+=L[0],\n'*x.pop(i:=0));print(len(a),*a)