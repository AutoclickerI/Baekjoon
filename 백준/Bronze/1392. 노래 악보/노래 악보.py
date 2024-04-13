N,Q,*t=map(int,input().split())
s=-1
for _ in[0]*N:s+=int(input());t+=s,
for i in[0]*Q:
 p=int(input())
 while t[i]<p:i+=1
 print(i+1)