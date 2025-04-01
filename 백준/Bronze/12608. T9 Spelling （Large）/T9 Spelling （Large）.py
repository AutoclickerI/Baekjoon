def get(c):
    a=[' ','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
    for i in range(10):
        if c in a[i]:
            return str(i)*-~a[i].find(c)

for T in range(1,int(input())+1):
    s=''
    for i in input().upper():
        c=get(i)
        if s and s[-1]==c[0]:
            s+=' '
        s+=c
    print(f'Case #{T}:',s)