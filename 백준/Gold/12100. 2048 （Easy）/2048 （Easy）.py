p=int(input())
L=[[[*map(int,input().split())]for _ in[0]*p]]
anslist=[]
for _ in[0]*5:
    for l in L:
        ans=[]
        for i in l:
            tmp=[j for j in i if j!=0]
            for j in range(len(tmp)-1):
                if tmp[j]==tmp[j+1]:
                    tmp[j]*=2
                    tmp[j+1]=0
            ans+=[([j for j in tmp if j!=0]+[0]*p)[:p]]
        anslist+=[ans]
        ans=[]
        for i in l:
            tmp=[j for j in i if j!=0][::-1]
            for j in range(len(tmp)-1):
                if tmp[j]==tmp[j+1]:
                    tmp[j]*=2
                    tmp[j+1]=0
            ans+=[([0]*p+[j for j in tmp[::-1] if j!=0])[-p:]]
        anslist+=[ans]
        ans=[]
        for i in zip(*l):
            tmp=[j for j in i if j!=0]
            for j in range(len(tmp)-1):
                if tmp[j]==tmp[j+1]:
                    tmp[j]*=2
                    tmp[j+1]=0
            ans+=[([j for j in tmp if j!=0]+[0]*p)[:p]]
        *ans,=zip(*ans)
        anslist+=[ans]
        ans=[]
        for i in zip(*l):
            tmp=[j for j in i if j!=0][::-1]
            for j in range(len(tmp)-1):
                if tmp[j]==tmp[j+1]:
                    tmp[j]*=2
                    tmp[j+1]=0
            ans+=[([0]*p+[j for j in tmp[::-1] if j!=0])[-p:]]
        *ans,=zip(*ans)
        anslist+=[ans]
    L=anslist
    anslist=[]
print(max(max(max(i)for i in l)for l in L))