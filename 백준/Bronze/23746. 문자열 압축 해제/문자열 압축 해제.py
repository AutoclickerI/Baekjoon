I=input
l=[I().split()for i in[0]*int(I())]
s=I()
for a,b in l:s=s.replace(b,a)
p,q=map(int,I().split())
print(s[p-1:q])