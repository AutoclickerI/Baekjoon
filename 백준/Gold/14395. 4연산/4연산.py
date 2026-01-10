s,t=map(int,input().split())
if s==t:
    print(0)
else:
    l=[('',s)]
    d={}
    for c,v in l:
        for i in'*+-/':
            if i=='*':
                n=v*v
            if i=='+':
                n=v+v
            if i=='-':
                n=0
            if i=='/':
                n=1
            if n not in d:
                if 0 in d and 1 in d and t<n:
                    continue
                d[n]=c+i
                l+=(c+i,n),
    print(d.get(t,-1))