M,T=map(int,input().split())
d={}
name=[]
for _ in[0]*T:
    N,K=input().split()
    if K[-1]=='%':
        u=M*int(K[:-1])//100
    else:
        u=min(M,int(K))
    M-=u
    c=0-u//-4
    for i in range(4):
        u-=c
        d[f'{N}{i+1}']=c if u>=0 else max(u+c,0)
        name+=f'{N}{i+1}',
if M:
    print('Invalid System')
else:
    s=input()
    if s in d:
        if d[s]:
            tmp=0
            for i in name:
                if i==s:
                    break
                tmp+=d[i]
            print(tmp+1,tmp+d[i])
        else:
            print('Liar')
    else:
        tmp=0
        tmp2=0
        for i in name:
            if i[:-1]!=s:
                tmp+=d[i]
            if i[:-1]==s:
                tmp2+=d[i]
            if i==s+'4':
                break
        if tmp2:
            print(tmp+1,tmp+tmp2)
        else:
            print('Liar')