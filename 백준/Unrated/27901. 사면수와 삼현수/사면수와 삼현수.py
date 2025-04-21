task=int(input())
N=int(input())

d={1:'do',
   2:'ke',
   3:'tur',
   4:'boi',
   5:'oro',
   6:'dare'}

p={0:'',
   1:'land',
   2:'tilej',
   3:'kzuen',
   4:'alkzuen'}

def to_7(n):
    s=0
    p=0
    while n:
        s+=n%7*10**p
        n//=7
        p+=1
    return s

if task==1:
    z=1
    n=to_7(N)
    l=[d[n%10]]if n%10 else[]
    n//=10
    while n:
        if n%10:
            l+=[d[n%10],''][n%10<2]+p[z],
        n//=10
        z+=1
    print(*l[::-1])
else:
    print(-1)