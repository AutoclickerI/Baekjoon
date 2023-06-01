a=list(input())
b=list(input())
c=[]
try:
    n=0
    while 1:
        k=a[n]
        c.append(k)
        try:
            if k==b[-1]:
                f=0
                for i in range(len(b)):
                    if c[-1-i]!=b[-1-i]:
                        f=1
                if f==0:
                    for i in range(len(b)):
                        c.pop()
        except:pass
        n+=1
except:0
print(''.join(c)if len(c)!=0 else'FRULA')