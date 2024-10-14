a=input()
if not a:
    a=input()
b=input()
if not b:
    b=input()
c=input()
if not c:
    c=input()
def check():
    for i in[a,b,c]:
        if not eval('d['+']+d['.join(i.split()[:4])+']'+i.split()[4].replace('=','==')+'d['+']+d['.join(i.split()[5:])+']'):
            return False
    return True
d={i:0 for i in range(1,13)}
ans=[]
for i in range(1,13):
    d[i]=1
    if check():
        ans+=f'{i}+',
    d[i]=-1
    if check():
        ans+=f'{i}-',
    d[i]=0

if len(ans)==1:
    print(*ans)
elif ans:
    print('indefinite')
else:
    print('impossible')