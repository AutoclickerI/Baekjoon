for C in range(int(input())):
    p,q=input().split()
    p=int(p)
    l=[[*map(int,input().split())]for _ in[0]*p]
    ans=[]
    if q=='left':
        for i in l:
            tmp=[j for j in i if j!=0]
            for j in range(len(tmp)-1):
                if tmp[j]==tmp[j+1]:
                    tmp[j]*=2
                    tmp[j+1]=0
            ans+=[([j for j in tmp if j!=0]+[0]*p)[:p]]
    if q=='right':
        for i in l:
            tmp=[j for j in i if j!=0][::-1]
            for j in range(len(tmp)-1):
                if tmp[j]==tmp[j+1]:
                    tmp[j]*=2
                    tmp[j+1]=0
            ans+=[([0]*p+[j for j in tmp[::-1] if j!=0])[-p:]]
    if q=='up':
        for i in zip(*l):
            tmp=[j for j in i if j!=0]
            for j in range(len(tmp)-1):
                if tmp[j]==tmp[j+1]:
                    tmp[j]*=2
                    tmp[j+1]=0
            ans+=[([j for j in tmp if j!=0]+[0]*p)[:p]]
        *ans,=zip(*ans)
    if q=='down':
        for i in zip(*l):
            tmp=[j for j in i if j!=0][::-1]
            for j in range(len(tmp)-1):
                if tmp[j]==tmp[j+1]:
                    tmp[j]*=2
                    tmp[j+1]=0
            ans+=[([0]*p+[j for j in tmp[::-1] if j!=0])[-p:]]
        *ans,=zip(*ans)
    print(f'Case #{C+1}:')
    for i in ans:print(*i)