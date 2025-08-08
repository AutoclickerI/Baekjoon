p,w=map(int,input().split())
t=q=0
for a in input():b=ord(a)-5-('R'<a)-('Y'<a);t+=p*(b%3-~(a in'SZ'))+w*(q==(q:=b//3)>9)
print(t)