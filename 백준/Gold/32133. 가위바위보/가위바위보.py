N,M,K=map(int,input().split())
l=zip(*eval('input(),'*N))
d={'R':'S','S':'P','P':'R'}
x=[[]for _ in[0]*N]
for idx,i in enumerate(l):
    s={}
    for j in range(N):
        x[j]+=i[j]
    for j in x:
        s[''.join(j)]=s.get(''.join(j),0)+1
    m=min(s.values())
    if m<=K:
        print(idx+1)
        for i in s:
            if s[i]==m:
                exit(print(''.join(d[j]for j in i)))
print(-1)