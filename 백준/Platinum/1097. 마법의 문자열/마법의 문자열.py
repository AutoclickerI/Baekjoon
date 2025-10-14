N=int(input())
l=[input()for _ in[0]*N]
K=int(input())
from itertools import*
cnt=0
for i in permutations(l,N):
    T=''.join(i)
    s=T*2
    pi=[0]
    j=0
    for i in range(1,len(T)):
        while j and T[j]!=T[i]:
            j=pi[j-1]
        if T[j]==T[i]:
            j+=1
        pi+=j,
    j=0
    v=0
    for i in range(len(s)-1):
        while j and T[j]!=s[i]:
            j=pi[j-1]
        if T[j]==s[i]:
            if j==len(T)-1:
                v+=1
                j=pi[j]
            else:
                j+=1
    cnt+=v==K
print(cnt)
