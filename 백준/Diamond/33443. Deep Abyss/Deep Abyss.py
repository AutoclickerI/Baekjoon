def gettype(i):
    neg=i[0]=='~'
    data=i[neg:]
    if data.isdigit():
        return int(data)
    if data.startswith('0x'):
        return eval(i)&2**128-1
    mat=dv.get(data,[0]*128)[:]
    if neg:
        for i in range(128):
            mat[i]^=1
    return mat

dv={'x':[1<<128-i for i in range(128)]}

for i in open(0):
    inp=i.split()
    if not inp:
        continue
    if len(inp)==3:
        v,_,t=inp
        t=gettype(t)
        if type(t)==list:
            dv[v]=t
        else:
            dv[v]=[*map(int,f'{t:0128b}')]
        continue
    v,_,lt,op,rt=inp
    if type(gettype(lt))!=list and op not in['<<','>>']:
        rt,lt=lt,rt
    mat=gettype(lt)
    rt=gettype(rt)
    if type(mat)==int:
        mat=[*map(int,f'{mat:0128b}')]
    match op:
        case '^':
            if type(rt)==list:
                for i in range(128):
                    mat[i]^=rt[i]
            else:
                for i,x in enumerate(f'{rt:0128b}'):
                    mat[i]^=int(x)
        case '&':
            for i,x in enumerate(f'{rt:0128b}'):
                if x<'1':
                    mat[i]=0
        case '|':
            for i,x in enumerate(f'{rt:0128b}'):
                if'0'<x:
                    mat[i]=1
        case '<<':
            mat=mat[rt:]+[0]*rt
        case '>>':
            mat=[0]*rt+mat[:128-rt]
        case _:
            raise
    dv[v]=mat

mat=gettype('x')

for i in range(128):
    mat[i]^=1<<128-i

#REF
for i in range(128):
    for j in range(128):
        if j<i:
            if mat[j]&(1<<128-i)and not mat[j]&(1<<128-j):
                break
        else:
            if mat[j]&(1<<128-i):
                break
    else:
        continue
    mat[i],mat[j]=mat[j],mat[i]
    for j in range(128):
        if j!=i and mat[j]&(1<<128-i):
            mat[j]^=mat[i]
#RREF
for i in range(128)[::-1]:
    if mat[i]&(1<<128-i)<1:
        continue
    for j in range(i):
        if mat[j]&(1<<128-i):
            mat[j]^=mat[i]

f=0

for i in range(128):
    if mat[i]&(1<<128-i)<1:
        f|=mat[i]
    elif 1<(mat[i]&-2).bit_count():
        j=i+1
        while mat[i]&(1<<128-j)<1:
            j+=1
        f|=mat[j]
        mat[j]=mat[i]^(1<<128-i)
        mat[i]=1<<128-i
        for v in range(j):
            if mat[v]&(1<<128-j):
                mat[v]^=mat[j]
n=0
for i in mat:
    n*=2
    n+=i%2

if f:
    print(':(')
else:
    print(hex(n))