N,K,B,*l=map(int,open(0).read().split())
print(sum(l[(B-1+i)%N]for i in range(K)))