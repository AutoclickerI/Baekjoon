n=int(input())+1
b=list(map(int,input().split()))
ans=[]
def check(z):
    z=[0]+z+[n]
    c=[]
    for j in range(1,len(z)):
        if abs(z[j-1]-z[j])!=1:
            c.append(j-1)
    return c
num=check(b)
try:
    for i in range(len(num)):
        for j in range(len(num)-i-1):
            d=b.copy()
            d=d[:num[i]]+list(reversed(d[num[i]:num[i+j+1]]))+d[num[i+j+1]:]
            if len(check(d))==2:
                ans.append(f'{num[i]+1} {num[i+j+1]}')
                a,b=check(d);ans.append(f'{a+1} {b}')
                raise
    a,b=check(b);ans.append(f'{a+1} {b}')
except:0
try:
    print(ans[0],ans[1],sep='\n')
except:
    try:
        d=b.copy()
        d=d[:num[0]]+list(reversed(d[num[0]:num[2]-1]))+d[num[2]-1:]
        if len(check(d))==2:
            ans.append(f'{num[0]+1} {num[2]-1}')
            a,b=check(d);ans.append(f'{a+1} {b}')
            raise
        else:
            d=b.copy()
            d=d[:num[0]+1]+list(reversed(d[num[0]+1:num[2]]))+d[num[2]:]
            if len(check(d))==2:
                ans.append(f'{num[0]+2} {num[2]}')
                a,b=check(d);ans.append(f'{a+1} {b}')
        a,b=check(b);ans.append(f'{a+1} {b}')
    except:0
    ans+=['1 1','1 1']
    print(ans[0],ans[1],sep='\n')