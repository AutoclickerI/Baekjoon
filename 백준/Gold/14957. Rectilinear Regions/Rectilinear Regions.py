n,m=map(int,input().split())
*l,=map(int,input().split())
yl=l[::2]
xl=l[1::2]
*l,=map(int,input().split())
yu=l[::2]
xu=l[1::2]
#%%
if yl!=sorted(yl)and yu!=sorted(yu):
    cnt=0
    area=0
    ptrl=0
    ptru=0
    posl=yl[0]
    posu=yu[0]
    positive=posu>=posl
    start=posu>posl
    tmp=0
    for i in range(50010):
        if ptru<m and xu[ptru]==i:
            ptru+=1
            posu=yu[ptru]
            if positive and posu<=posl:
                if not start:
                    area+=tmp
                    cnt+=0<tmp
                start=0
                tmp=0
                positive=0
        if ptrl<n and xl[ptrl]==i:
            ptrl+=1
            posl=yl[ptrl]
            if not positive and posl<=posu:
                start=0
                positive=1
        tmp+=max(0,posu-posl)
    print(cnt,area)
else:
    cnt=0
    area=0
    ptrl=0
    ptru=0
    posl=yl[0]
    posu=yu[0]
    positive=posu>=posl
    start=posu>posl
    tmp=0
    for i in range(50010):
        if ptrl<n and xl[ptrl]==i:
            ptrl+=1
            posl=yl[ptrl]
            if positive and posu<=posl:
                if not start:
                    area+=tmp
                    cnt+=0<tmp
                start=0
                tmp=0
                positive=0
        if ptru<m and xu[ptru]==i:
            ptru+=1
            posu=yu[ptru]
            if not positive and posl<=posu:
                start=0
                positive=1
        tmp+=max(0,posu-posl)
    print(cnt,area)