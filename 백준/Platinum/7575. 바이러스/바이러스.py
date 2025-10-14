l=[]
N,K=map(int,input().split())
input()
s=input().split()
for i in range(len(s)-K+1):
    l+=' '.join(s[i:i+K]),

for _ in[0]*~-N:
    input()
    s=input()
    s+='_'+' '.join(s.split()[::-1])
    tmp=[]
    for i in l:
        if i in s:
            tmp+=i,
    l=tmp

if l:
    print('YES')
else:
    print('NO')