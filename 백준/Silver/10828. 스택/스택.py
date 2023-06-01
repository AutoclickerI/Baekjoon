import sys
L=[]
input=sys.stdin.readline
for i in[0]*int(input()):
    c=input().split()
    if c[0]=='push':
        L+=[c[1]]
    elif c[0]=='top':
        try:print(L[-1])
        except:print(-1)
    elif c[0]=='size':
        print(len(L))
    elif c[0]=='empty':
        print(+(len(L)<1))
    elif c[0]=='pop':
        try:print(L.pop())
        except:print(-1)