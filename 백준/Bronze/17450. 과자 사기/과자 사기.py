l=[]
for _ in'000':p,q=map(int,input().split());l+=[q/(p-5*(p>499))]
print('SNU'[l.index(max(l))])