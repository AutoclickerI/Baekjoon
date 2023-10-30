N,K,M=map(int,input().split())
l=[[*map(int,input().split())][1:]for _ in[0]*K]
*ll,=map(int,input().split())
print(-sum(sum(ll[i-1]for i in I)//-M for I in l))