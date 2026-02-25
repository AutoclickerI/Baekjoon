N=int(input())
vis=[int(input().replace(' ','')[::-1],2)for _ in[0]*N]

w1,w2=map(int,input().split())
W=1<<N

real=int(input().translate({87:49,66:48})[::-1],2)

alive=[w1<=w.bit_count()<=w2 for w in range(W)]

s0=[0]*W
s1=[0]*W
s=0

for _ in[0]*int(input()):
    tmp=alive[:]
    r=''
    for i in input().split()[1:]:
        s+=1
        vm=vis[i:=int(i)-1]
        bi=1<<i
        for w in range(W):
            if alive[w]:
                obs=w&vm
                if w&bi:
                    s1[obs]=s
                else:
                    s0[obs]=s
        
        obs_real=real&vm
        ansY=(s0[obs_real]==s)^(s1[obs_real]==s)
        
        r+='NY'[ansY]
        
        for w in range(W):
            if tmp[w]:
                obs=w&vm
                tmp[w]&=(s0[obs]==s)^(s1[obs]==s)==ansY

    print(r)
    alive=tmp