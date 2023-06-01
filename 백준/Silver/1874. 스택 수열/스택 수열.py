n,*l=map(int,open(0))
l2=[*range(1,n+1)]
stack=[-1]
a=''
try:
    while l:
        n=l.pop(0)
        t=stack[-1]
        while t!=n:
            t=l2.pop(0)
            a+='+'
            stack+=[t]
        a+='-'
        stack.pop()
    print(*a)
except:
    print('NO')