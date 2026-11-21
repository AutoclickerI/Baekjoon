print(sum(abs(n-v[len(v)//2])for v in
map(sorted,zip(*[map(int,i.split())for i in open(0)][1:]))for n in v))