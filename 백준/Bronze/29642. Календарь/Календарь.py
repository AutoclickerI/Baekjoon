f=lambda:[*map(int,input().split())]
n,k,*b=f()
d=f()
if k>0:b=f()
db=[len({*str(b)}&{*str(i+1)})>0 for i in range(max(d))]
s=[0]
for i in db:s+=s[-1]+i,
print(sum(s[i]for i in d))