while 1:
 n,b=map(int,input().split())
 if n==0:break
 blist=list(map(int,input().split()))
 poss=[1]+[0]*n
 for i in range(b):
  for j in range(i+1,b):
   temp=abs(blist[i]-blist[j])
   if temp<=n:poss[temp]+=1
 n-=1
 if 0 in poss:print('N')
 else:print('Y')