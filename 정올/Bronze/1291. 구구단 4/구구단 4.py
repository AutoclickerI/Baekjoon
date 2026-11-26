while 1:
    s,e=map(int,input().split())
    if 1<s<10>e>1:break
    print('INPUT ERROR!')
for i in range(1,10):
    r=''
    for j in[*range(s,e+1)]or range(s,e-1,-1):
        r+=f'{j} * {i} = {i*j:2}   '
    print(r.strip())