c=1e9
print(*[c:=min(c+1,int(n))for n in[*open(0)][1].split()])