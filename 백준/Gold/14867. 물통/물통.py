a,b,c,d=map(int,input().split())
if c in[0,a]and d in[0,b]:
    print((0<c)+(0<d))
elif c in[0,a]:
    # fill b d
    # a=>b
    ans=[]
    try:
        for k in range(a):
            if(d+b*k)%a<1:
                break
        else:
            raise
        v=d+b*k
        ans+=max(v//a*2+k*2+(0<c),0),
    except:0
    # b=>a
    try:
        for k in range(b):
            if(d+a*k)%b<1:
                break
        else:
            raise
        v=d+a*k
        ans+=max((v-d)//a*2-v//-b-(0<c),0),
    except:0
    print(min(ans or[-1]))
    
elif d in[0,b]:
    # fill a c
    # a=>b
    ans=[]
    try:
        for k in range(a):
            if(c+b*k)%a<1:
                break
        else:
            raise
        v=c+b*k
        ans+=max(v//a*2+v//b-(0<d),0),
    except:0
    # b=>a
    try:
        for k in range(b):
            if(c+a*k)%b<1:
                break
        else:
            raise
        v=c+a*k
        ans+=max((v-c)//a*2+v//b*2+(0<d),0),
    except:0
    print(min(ans or[-1]))
    
else:
    print(-1)