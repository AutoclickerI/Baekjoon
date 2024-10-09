s=[0,0]
b,t,*r=0,1
for i in[*open(0)][1:]:n=int(i)-1;r+=[s[:]]*(n!=b);b=n;s[n]+=1;t+=(s[0]==s[1])
r+=s,
print(*s,t,max([sum(j)-sum(i)for i,j in zip(r,r[1:])if(i[0]-i[1])*(j[0]-j[1])<0]))