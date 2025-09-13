n,d,k =map(int,input().split())
i,j = 0,1
r = [(0,0)]
def f():(p,*_,q),(u,*_,v)=map(sorted,zip(*r));exit(print(q-p+1,v-u+1,*map(''.join,[['.*'[(x,y)in r]for y in range(u,v+1)]for x in range(p,q+1)][::-1])))
h=1
while 1:
    for _ in range(d):
        r += (r[-1][0]+i,r[-1][1]+j),
        n -= 1
        n or f()
    i,j = j,-i
    h^=1
    d*=h*~-k+1