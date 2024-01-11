while(s:=input())>'1':
    m,n=map(int,s.split())
    max_safe=1
    min_break=n
    for _ in[0]*m:
        p,q=input().split()
        if q[0]<'D':
            min_break=min(min_break,int(p))
        else:
            max_safe=max(max_safe,int(p))
    print(min(max_safe+1,n),max(1,min_break-1))