[[*t1]]=ans=[input()]
*t2,=input()
f=t1[0]=='2'!=t2[0]
for i in 4,3,f^1,f:
    t1[i],t2[i]=int(t1[i]),int(t2[i])
    while t1[i]-t2[i]:t1[i]=(t1[i]+[(t1[i]<t2[i])*2-1,1-(t2[i]-t1[i])%10//5*2][i%3==1])%10;ans+=t1[:],
print(len(ans))
for i in ans:print(*i,sep='')