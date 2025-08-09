m=1e9
print(sum(m>(m:=min(m,v))for _,v in sorted([*map(int,i.split())]for i in[*open(0)][1:])))