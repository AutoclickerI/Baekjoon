_,*l=[[*map(int,i.split())]for i in open(0)]
i=0
while i<2e5*any(T<R*-~-(T<=i%H<=R)or R<i%H<T for H,R,T in l):i+=1
print([i,'impossible'][i==2e5])