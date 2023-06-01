a,b=map(int,input().split())
c=[0]
for i in range(1,a+1):
 if a%i==0:c+=[i]
try:print(c[b])
except:print(0)