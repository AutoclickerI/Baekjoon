x=-1
print(sum(h>x<(x:=h)for h in[*map(int,open(0))][:0:x]))