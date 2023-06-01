a,b,c,d=map(int,input().split())
if a>b:a,b=b,a
if c>d:c,d=d,c
print(max(b,d)-min(a,c)+min(1,2+b-c,2+d-a))