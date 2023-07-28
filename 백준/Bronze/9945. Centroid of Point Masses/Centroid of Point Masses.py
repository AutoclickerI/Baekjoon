i=0
while(s:=int(input()))>0:
    i+=1
    M=X=Y=0
    for _ in[0]*s:
        x,y,m=map(int,input().split())
        M+=m
        X+=x*m
        Y+=y*m
    print(f'Case {i}: {X/M:.2f} {Y/M:.2f}')
    input()