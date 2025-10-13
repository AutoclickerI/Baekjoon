import math
for i in[*open(0)][:-1]:
    p,q=i.split()
    n=math.gcd(len(p),len(q))
    p+=q
    chunk=p[:n]
    for i in range(0,len(p),n):
        if p[i:i+n]!=chunk:
            break
    else:
        print(z:=len(q)//n,len(p)//n-z)
        continue
    print('NAO')