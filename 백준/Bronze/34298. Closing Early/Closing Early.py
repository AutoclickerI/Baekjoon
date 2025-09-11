R,S,N,*l=map(int,open(0).read().split())
i=c=0
try:
 while R-c%S:c+=l[i];i+=1
except:i=-1
print(i)