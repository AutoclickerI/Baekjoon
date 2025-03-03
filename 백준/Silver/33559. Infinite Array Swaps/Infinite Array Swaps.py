input()
a=sorted(map(int,input().split()))
b=sorted(map(int,input().split()))
aa=[]
ba=[]
at=[]
bt=[]
while a and b:
    if a[-1]==b[-1]:
        aa+=a.pop(),
        ba+=b.pop(),
    elif a[-1]<b[-1]:
        bt+=b.pop(),
    else:
        at+=a.pop(),
at+=a
bt+=b
aa+=at
ba+=bt
print(sum(i==j for i,j in zip(aa,ba)))
print(*aa)
print(*ba)