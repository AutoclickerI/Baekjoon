import sys
input=sys.stdin.readline
N,K,C,R=map(int,input().split())
skill=[0]*K
*base,=map(int,input().split())
*s,=map(int,input().split())
*p,=map(int,input().split())
stardust=0
tired=0
combo=0
for _ in[0]*N:
    i=int(input())-1
    if i<0:
        tired=max(0,tired-R)
        combo=0
    else:
        stardust+=(base[i]*(100+combo*C)*(100+skill[i]*s[i]))//10000
        combo+=1
        tired+=p[i]
        skill[i]+=1
    if tired>100:
        exit(print(-1))
print(stardust)