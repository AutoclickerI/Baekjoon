import sys
input=sys.stdin.readline
for I in range(int(input())):
    n,m,T=map(int,input().split())
    D=[0]*n
    for _ in[0]*m:
        i,t,d=map(eval,input().split())
        if 0<=T-t<1000:
            D[i-1]+=d
    v=[1/(1+i/10000)for i in D]
    Y=N=0
    for i in v:
        if input()=='Y\n':
            Y+=1
        else:
            N+=i
    print(f'Data Set {I+1}:\n{Y:.2f} {N:.2f}\n')