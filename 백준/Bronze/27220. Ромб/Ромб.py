n,a,b=map(int,open(0))
l=[n*['.']for _ in[0]*n]
for i in range(n):
    for j in range(n):
        if a<=abs(i-n//2)+abs(j-n//2)<=b:
            l[i][j]='*'
for i in l:print(*i,sep='')