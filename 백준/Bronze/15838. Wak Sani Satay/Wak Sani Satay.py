l=[.8-15.5/85,1-32/85,1.2-40/85,0.6]
c=0
while s:=int(input()):
    c+=1
    print(f'Case #{c}: RM{sum(sum(i*int(j)for i,j in zip(l,input().split()))for _ in[0]*s):.2f}')
