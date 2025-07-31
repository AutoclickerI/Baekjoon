N,*l=open(0)
N=int(N)
print((sum(min(int(i.translate({48:57,54:57})),100)for i in l)+N//2)//N)