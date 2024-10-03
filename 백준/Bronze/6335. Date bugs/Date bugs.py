T=1
R=range
while n:=int(input()):
    l=[0]*10000
    for i in R(n):
        y,a,b=map(int,input().split())
        for j in R(y,10000,b-a):l[j]+=1
    try:p=f'The actual year is {next(i for i in R(10000)if l[i]==n)}'
    except:p='Unknown bugs detected'
    print(f'Case #{T}:\n{p}.\n');T+=1