import sys
input=sys.stdin.readline

N,K,M=map(int,input().split())
l=[4*[0]for _ in[0]*4]
s=[0]*4
for _ in[0]*N:
    a1,a2,a3,a4,s1,s2,s3,s4=map(int,input().split())
    l[a1-1][0]+=1
    l[a2-1][1]+=1
    l[a3-1][2]+=1
    l[a4-1][3]+=1
    s[a1-1]+=s1
    s[a2-1]+=s2
    s[a3-1]+=s3
    s[a4-1]+=s4

def check():
    cnt=1
    for i in range(4):
        if s_f[K-1]<s_f[i] or (s_f[K-1]==s_f[i] and i<K-1):
            cnt+=1
    return M==cnt

for d4 in range(-100,101):
    for d3 in range(d4,101):
        for d2 in range(d3,min(101,101-d3-d4)):
            d1=-d2-d3-d4
            if d1<-100 or 100<d1 or d1<d2:
                continue
            s_f=s[:]
            for i in range(4):
                s_f[i]+=sum(p*q for p,q in zip(l[i],[d1,d2,d3,d4]))
            if check():
                exit(print(d1,d2,d3,d4))
print(-1)