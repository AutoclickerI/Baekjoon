f=lambda:[*map(int,input().split())]

n,a,b=f()
*costs,=eval('f(),'*n)

if n==1:print('%.2f'%max(a/costs[0][0],b/costs[0][1]))
else:tmp=costs[:];print('%.2f'%max(a/tmp.pop(tmp.index(min(tmp,key=lambda x:(x[0],-x[1]))))[0]+b/min(tmp,key=lambda x:x[1])[1],b/costs.pop(costs.index(min(costs,key=lambda x:(x[1],-x[0]))))[1]+a/min(costs)[0]))