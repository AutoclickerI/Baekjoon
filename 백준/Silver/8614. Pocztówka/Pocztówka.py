n,m,*l=map(int,open(t:=0).read().split())
print(sum(t:=[i,t][h<m]for i,h in enumerate(l,1)))