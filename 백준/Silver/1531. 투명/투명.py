d={}
[N,M],*l=[map(int,i.split())for i in open(0)]
for x1,y1,x2,y2 in l:
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            d[x,y]=d.get((x,y),0)+1
print(sum(M<d[i]for i in d))