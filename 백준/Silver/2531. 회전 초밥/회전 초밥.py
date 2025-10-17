N,d,k,c,*l=map(int,open(0).read().split())
l*=2
print(max(len({*l[i:i+k],c})for i in range(N)))