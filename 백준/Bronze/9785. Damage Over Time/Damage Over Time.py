(N,M),*l=[[*map(int,i.split())]for i in open(0)]
l=sorted(l)[:~M:-1]
print(sum(i[0]for i in l),min(i[1]for i in l))