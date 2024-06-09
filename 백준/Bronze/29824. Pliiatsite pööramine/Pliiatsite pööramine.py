s=[*open(0)][1]
i=s[0]
a=[]
for k,j in enumerate(s,1):
    if j!=i:a+=k,
    i=j
print(len(a)//2)
while len(a)>1:
    p,q,*a=a
    print(f'{p}-{q-1}')