n,p,q=map(int,input().split())
l=[tuple(map(int,input().split()))for _ in[0]*n]
p-=1
q-=1
print('HAANPGPRYY'[max(l[p]+[*zip(*l)][q])!=l[p][q]::2])