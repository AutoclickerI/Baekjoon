d={input():0for _ in[0]*int(input())}
prev=0
for _ in[0]*int(input()):
    p,q,r=input().replace(*': ').split()
    d[r]-=prev-(prev:=int(p)+int(q))
print(m:=max(d,key=lambda s:d[s]),d[m])