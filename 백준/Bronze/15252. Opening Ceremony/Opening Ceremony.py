I=lambda:map(int,input().split())
for i in range(int(input())):
    c,n,*l=*I(),*I()
    for j in I():l[j-1]-=1
    print(f'Data Set {i+1}:\n{max(l)}\n')