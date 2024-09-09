N=int(input())
s,e=1,N
while 1<N:
    sep=(N+2)//3
    print('?',*range(s,s+sep),0,*range(s+sep,s+sep*2),0)
    v=input()
    if v=='=':
        N-=2*sep
        s+=2*sep
    if v=='>':
        N=sep
        s+=sep
        e=s+sep-1
    if v=='<':
        N=sep
        e=s+sep-1
print('!',s)