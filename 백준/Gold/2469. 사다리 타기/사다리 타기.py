k=int(input())
n=int(input())
*l,=[chr(i+65)for i in range(k)]
*e,=input()
f=0
q=[[],[]]
for _ in[0]*n:
    s=input()
    if{*s}=={'?'}:
        f=1
        continue
    else:
        q[f]+=s,
for s in q[0]:
    for i,c in enumerate(s):
        if c=='-':
            l[i:i+2]=l[i+1],l[i]
for s in q[1][::-1]:
    for i,c in enumerate(s):
        if c=='-':
            e[i:i+2]=e[i+1],e[i]

s=''
for i in range(k-1):
    if l[i]!=e[i]:
        s+='-'
        e[i:i+2]=e[i+1],e[i]
    else:
        s+='*'
if l==e:
    print(s)
else:
    print('x'*~-k)