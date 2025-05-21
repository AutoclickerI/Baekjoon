from heapq import*
_,*x=map(int,open(0).read().split())
while x:
    n=x.pop(0);l=x[:n];x=x[n:];S=[];L=[];a=[]
    for i in l:
        heappush(L,i)
        heappush(S,-heappop(L))
        if len(L)<len(S):heappush(L,-heappop(S));a+=L[0],
    print(len(a),*a)