s=sorted(map(int,[*open(0)][1].split()))
print(m:=min(a:=[j-i for i,j in zip(s,s[1:])]),a.count(m))