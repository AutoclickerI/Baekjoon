l=[]
for i in range(int(input())):l+=[input().split()]
s=input()
for h in l:s=s.replace(h[1],h[0])
p,q=map(int,input().split())
print(s[p-1:q])