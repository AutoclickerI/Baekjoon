N,t=map(int,input().split())
if t:
    print('!',N//2+1)
    print(1,1)
    for _ in(N//2-1)*[0]:
        s,e=map(int,input().split())
        print(e,s)
else:
    print('!',N//2)
    for _ in N//2*[0]:
        s,e=map(int,input().split())
        print(e,s)