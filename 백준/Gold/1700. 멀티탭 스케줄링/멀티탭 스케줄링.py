N,K=map(int,input().split())
*l,=map(int,input().split())
l+=range(K+1)

cnt=0
s=set()
for i in range(K):
    s|={l[i]}
    if N<len(s):
        m=min(s,key=lambda v:-l[i:].index(v))
        cnt+=1
        s-={m}
print(cnt)