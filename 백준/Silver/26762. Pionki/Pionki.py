s,*l=open(0)
N,M=map(int,s.split())
print(sum(sorted(map(str.count,l,'#'*N))[:-1]+sorted(map(tuple.count,zip(*l),'#'*M))[:-1]))