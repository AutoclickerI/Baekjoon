import sys
input=sys.stdin.readline

for T in range(int(input())):
    print(f'Case #{T+1}:')
    a,b,x,m,n=map(int,input().split())
    q=int(input())
    db=[[0]*6]
    for _ in[0]*n:
        tmp=[0]*6
        for i in range(1,6):
            tmp[i]=(db[-1][i]*a+tmp[i-1]*b+x)%m
        db+=tmp,
    for _ in[0]*q:
        inst,*l=input().split()
        if inst=='insert':
            db+=[0,*map(int,l)],
        if inst=='remove':
            r=int(l[0])
            try:
                db[r][0]=1
            except:0
        if inst=='max':
            c=int(l[0])
            print(max(v[c]for v in db[1:]if v[0]<1))
        if inst=='min':
            c=int(l[0])
            print(min(v[c]for v in db[1:]if v[0]<1))
        if inst=='range':
            c,a,b=map(int,l)
            print(sum(a<=v[c]<=b for v in db[1:]if v[0]<1))