n,s,k=map(int,input().split())
l=[0]*n
for i in input().split():l[-1-int(i)//-s]+=1
m=max(l)
l=[('.'*m+'#'*i+'-')[~m:]for i in l]
for i in zip(*l):print(*i,sep='')