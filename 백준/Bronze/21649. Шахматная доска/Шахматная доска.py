m,n,*l=map(int,input().split())
print(m*n%2*'bwlhaictke'[sum(l)%2::2]or'equal')