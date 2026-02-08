N,A,B,C,*D=map(int,open(0).read().split())
for d in sorted(D)[::-1]:
 if C*B<d*A:A+=B;C+=d
print(C//A)