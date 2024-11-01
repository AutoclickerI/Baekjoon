N,M,R=map(int,input().split())
l=[]
for i in range(N):
    l+=[input(),i+1],
while'P'not in l[-1][0]:
    sl,nl=l.pop()
    if nl==R:
        exit(print(len(l)+1))
while l:
    s=input()[13:]
    if s[0]=='w':
        l[-1][0]=l[-1][0].replace('P','R',1)
    else:
        sl,nl=l.pop()
        sl=sl.replace('P','A',1)
        up=len(s)-6
        l[:len(l)-up]+=[sl,nl],
    
    while'P'not in l[-1][0]:
        sl,nl=l.pop()
        if nl==R:
            exit(print(len(l)+1))