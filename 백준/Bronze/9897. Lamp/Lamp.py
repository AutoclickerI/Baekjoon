s=open(0).read()
assert s[-2]!='\n\n'

s=s.split('\n')[:-1]
iterator=iter(s)

input=lambda:next(iterator)

l,g,r=map(int,input().split())
p={}
d=[0]*l
for n,a,b in eval('input().split(),'*g):p[n]=int(a)-1,int(b)
for n in eval('input(),'*r):
 for i in range(p[n][0],l,p[n][1]):d[i]^=1
print(sum(d))