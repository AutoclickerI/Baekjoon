s=sum(l:=[*map(int,[*open(0)][1].split())])
print(sum(i*(s:=s-i)for i in l)%(10**9+7))