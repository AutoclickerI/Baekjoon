M=1
n,_,*l=map(eval,open(P:=0).read().split())
x=n*[1]
y=n*[0]
while l:a,b,c,*l=l;c^=b;y[-a]|=c<<b;x[-a]&=c
print(sum(i>2for i in y),sum(x))