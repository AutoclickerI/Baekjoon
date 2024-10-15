a,b=map(int,input().split())
s,t=a,b
c=2
while 1:c+=1;s,t=t,(s+t)%10;(s,t)==(a,b)<exit(print(c))