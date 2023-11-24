_,g,r=map(int,input().split())
*l,=map(int,input().split())
t=0
T=0
while l:
    t+=l[0]
    if t>g:
        T=(l[0]-t-T)//(g+r)*(-g-r)
        t=0
    else:
        l.pop(0)
print(T+t)