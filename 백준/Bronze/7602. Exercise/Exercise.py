T=0
while N:=int(input()):
    T+=1
    l=eval('int(input()),'*N)
    print('Machine',T)
    while'$'<(s:=input()):
        s,n=s.split()
        print(s,sum(l[a-1]*t for a,t in eval('map(int,input().split()),'*int(n))))