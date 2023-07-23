for k in range(int(input())):
    n,W,E=map(int,input().split())
    hap=0
    for _ in[0]*n:
        p,q,r,s=map(int,input().split())
        hap+=max(W*p+E*r,W*q+E*s)
    print(f'Data Set {k+1}:\n{hap}\n')