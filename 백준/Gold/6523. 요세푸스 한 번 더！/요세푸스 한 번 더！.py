for i in[*open(0)][:-1]:
    N,a,b=map(int,i.split())
    s={0:0}
    x=0
    while s.get(x,0)<3:
        s[x]=s.get(x,0)+1
        x=(a*x*x+b)%N
    print(N-sum([1<s[i]for i in s]))