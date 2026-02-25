from math import gcd
a,b=map(int,input().split('/'))
c,d=map(int,input().split('/'))
e=a*d-c*b
f=b*d
g=gcd(e,f)
e//=g
f//=g
h=e//f
h+=e<0 and e%f!=0
if h==0 and e<0:
    print('-0')
else:
    print(h)
if e>0:
    if e-h*f:
        print(f'{e-(h*f)}/{f}')
        i=str(e-(h*f))
    else:
        exit()
else:
    if h*f-e:
        print(f'{-e+(h*f)}/{f}')
        i=str(-e+(h*f))
    else:
        exit()
if h==0:
    h='-'[e:]
else:
    h=str(h)
f=str(f)
'''
  i
h----
  f
'''
j=len(h)+max(len(i),len(f))
print(' '*(j-len(i))+i)
print(h+'-'*(j-len(h)))
print(' '*(j-len(f))+f)