p,q,r=open(0)
print(len(q)+~abs(int(p)-sum(i==j for i,j in zip(q,r))+1))