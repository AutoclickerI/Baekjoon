p,w=map(int,input().split())
t=q=0
for a in input():b=ord(a)-8-('R'<a)-('Y'<a);e=b%3-~(a in'SZ');t+=p*e+w*(q==b//3)*(8<q);q=b//3
print(t)