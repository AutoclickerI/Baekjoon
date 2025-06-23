ans=[input()]
t1=[*ans[0]]
*t2,=input()
f=t1[0]=='2'!=t2[0]
for i in 4,3,f^1,f:
    t1[i],t2[i]=int(t1[i]),int(t2[i])
    if i%3==1:
        while t1[i]-t2[i]:
            t1[i]=(t1[i]+1-(t2[i]-t1[i])%10//5*2)%10
            ans+=''.join(map(str,t1)),
    else:
        while t1[i]-t2[i]:
            t1[i]+=(t1[i]<t2[i])*2-1
            ans+=''.join(map(str,t1)),
print(len(ans))
for i in ans:print(i)