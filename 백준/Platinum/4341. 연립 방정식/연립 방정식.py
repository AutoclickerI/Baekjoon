from fractions import*
def gauss(x):
    for i in range(len(x)):
        x[i]=[x[i][j]/x[i][i]for j in range(len(x[0]))]
        for j in range(i+1,len(x)):
            try:
                x[j]=[x[j][k]-x[i][k]*(x[j][i]/x[i][i])for k in range(len(x[0]))]
            except:
                cache=x[i]
                del x[i]
                x+=[cache]
                x[j]=[x[j][k]-x[i][k]*(x[j][i]/x[i][i])for k in range(len(x[0]))]
    for i in range(len(x)-1,0,-1):
        x[i]=[x[i][j]/x[i][i]for j in range(len(x[0]))]
        for j in range(i-1,-1,-1):
            while 1:
                try:
                    x[j]=[x[j][k]-x[i][k]*(x[j][i]/x[i][i])for k in range(len(x[0]))]
                    break
                except:
                    cache=x[i]
                    del x[i]
                    x+=[cache]
    return x
for i in[0]*int(input()):
    p=input().split('=')
    q=input().split('=')
    try:input()
    except:0
    d1={'x':0,'y':0,'I':0}
    d2={'x':0,'y':0,'I':0}
    j=p[0].split()
    pos=1
    for P in range(len(j)):
        k=j[P]
        if P%2==0:
            try:
                d1['I']+=int(k)*pos
            except:
                try:
                    d1[k[-1]]+=int(k[:-1])*pos
                except:
                    try:
                        if k[-2]=='-':
                            d1[k[-1]]+=-pos
                    except:
                        d1[k[-1]]+=pos
        else:
            if k=='-':
                pos=-1
            else:
                pos=1
    j=p[1].split()
    pos=1
    for P in range(len(j)):
        k=j[P]
        if P%2==0:
            try:
                d1['I']-=int(k)*pos
            except:
                try:
                    d1[k[-1]]-=int(k[:-1])*pos
                except:
                    try:
                        if k[-2]=='-':
                            d1[k[-1]]-=-pos
                    except:
                        d1[k[-1]]-=pos
        else:
            if k=='-':
                pos=-1
            else:
                pos=1
    j=q[0].split()
    pos=1
    for P in range(len(j)):
        k=j[P]
        if P%2==0:
            try:
                d2['I']+=int(k)*pos
            except:
                try:
                    d2[k[-1]]+=int(k[:-1])*pos
                except:
                    try:
                        if k[-2]=='-':
                            d2[k[-1]]+=-pos
                    except:
                        d2[k[-1]]+=pos
        else:
            if k=='-':
                pos=-1
            else:
                pos=1
    j=q[1].split()
    pos=1
    for P in range(len(j)):
        k=j[P]
        if P%2==0:
            try:
                d2['I']-=int(k)*pos
            except:
                try:
                    d2[k[-1]]-=int(k[:-1])*pos
                except:
                    try:
                        if k[-2]=='-':
                            d2[k[-1]]-=-pos
                    except:
                        d2[k[-1]]-=pos
        else:
            if k=='-':
                pos=-1
            else:
                pos=1
    l=[list(map(Fraction,[d1['x'],d1['y'],-d1['I']])),list(map(Fraction,[d2['x'],d2['y'],-d2['I']]))]
    try:
        ans=gauss(l)
        for i in ans:
            print(i[-1])
        print()
    except:
        try:
            l=l[::-1]
            ans=gauss(l)
            for i in ans:
                print(i[-1])
            print()
        except:
            if d1['x']==0 and d2['x']!=0:
                d1,d2=d2,d1
            if d1['x']==0 and d2['x']==0:
                if d1['y']!=0 and d2['y']==0:
                    d1,d2=d2,d1
            No=False
            if d1['x']==0 and d1['y']==0 and d1['I']!=0:
                No=True
            if d2['x']==0 and d2['y']==0 and d2['I']!=0:
                No=True
            try:
                if d1['x']==0 and d2['x']==0 and Fraction(-d2['I'],d2['y'])!=Fraction(-d1['I'],d1['y']):
                    No=True
            except:0
            try:
                if d1['y']==0 and d2['y']==0 and Fraction(-d2['I'],d2['x'])!=Fraction(-d1['I'],d1['x']):
                    No=True
            except:0
            if No:
                print('don\'t know\ndon\'t know')
            else:
                if d1['x']!=0 and d1['y']==0:
                    print(Fraction(-d1['I'],d1['x']))
                else:
                    print('don\'t know')
                if d2['y']!=0 and d2['x']==0:
                    print(Fraction(-d2['I'],d2['y']))
                else:
                    print('don\'t know')
            print()