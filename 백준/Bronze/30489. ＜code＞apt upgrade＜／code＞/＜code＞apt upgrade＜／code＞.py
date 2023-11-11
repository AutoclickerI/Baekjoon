n,a,b,*c=map(int,open(0).read().split())
print(sum(sorted(c)[-a-b:])*100/sum(c))