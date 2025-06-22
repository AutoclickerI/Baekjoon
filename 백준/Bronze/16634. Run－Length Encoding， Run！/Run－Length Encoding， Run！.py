q,s=input().split()
l=[]
p=c=[]
for i in s:
 if p==(p:=i):c[-1]+=1
 else:c+=1,;l+=i,
for i,j in zip(*[[iter(s)]*2,(l,c)][f:='D'<q]):print(end=[i*int(j),i+str(j)][f])