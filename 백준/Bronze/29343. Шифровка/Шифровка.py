n=int(input())
w=input().lower()
h=t=a=0
v='aeiou'
for i in range(n):h+=w[i]in v;t+=w[~i]in v;a+=h==t>0
print(a)