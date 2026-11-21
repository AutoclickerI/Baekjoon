_,q=open(0)
print(sum(i!=j for i,j in zip(q,q[-2::-1]))//2)