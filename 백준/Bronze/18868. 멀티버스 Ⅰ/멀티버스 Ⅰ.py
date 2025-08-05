d={}
for s in open(a:=0):s=s.split();i=*[sum(int(j)<int(i)for j in s)for i in s],;v=d.get(i,0);a+=v;d[i]=v+1
print(a)