S=sorted
N,M,K,*l=open(0).read().split()
print(''.join(S(sum(S(S(i)for i in l)[:int(K)],[]))))