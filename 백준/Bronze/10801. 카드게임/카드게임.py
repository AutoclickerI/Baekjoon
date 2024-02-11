g=lambda:map(int,input().split())
t=sum((x>y)-(x<y)for x,y in zip(g(),g()))
print('DAB'[(t>0)-(t<0)])