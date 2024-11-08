import sys
input=sys.stdin.readline

N=int(input())
M=int(input())

stack=[]
for _ in[0]*N:
    a,v=map(int,input().split())
    if stack and stack[-1][0]==a:
        if stack[-1][1]<v:
            stack.pop()
            stack+=(a,v),
    else:
        stack+=(a,v),
l=[]
for a,v in stack:
    if not l and v<0:
        continue
    if l:
        tmp=l.pop()
        while l and tmp[1]<0 and tmp[0]!=v:
            tmp2=l.pop()
            if 0<=tmp2[1]:
                l+=tmp2,
                break
            if tmp[1]<tmp2[1]:
                tmp=tmp2
        l+=tmp,
    if 1<len(l) and l[-1][1]<0 and l[-2][0]==a:
        s=(a,max(l[-2][1]+l[-1][1]+v,l[-2][1],v))
        l.pop()
        l.pop()
        l+=s,
    else:
        l+=(a,v),

print(sum(i for _,i in l if 0<i))  