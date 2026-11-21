(_,L,K),*l=[map(int,i.split())for i in open(0)]
print(-sum(sorted(5*(L<i)-7+2*(L<j)for i,j in l)[:K])*20)