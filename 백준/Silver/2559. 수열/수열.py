p,q,*r=map(int,open(0).read().split())
print(max([s:=sum(r[:q])]+[s:=s+r[i+q]-r[i]for i in range(p-q)]))