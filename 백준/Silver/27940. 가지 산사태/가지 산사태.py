_,M,K,*l=map(int,open(o:=0).read().split())
for i in range(M):o+=l[2*i+1];K>=o or exit(print(i+1,1))
print(-1)